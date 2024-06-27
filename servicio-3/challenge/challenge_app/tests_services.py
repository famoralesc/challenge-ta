# tests.py

from django.test import TestCase
from unittest.mock import patch, MagicMock
from challenge_app.services import (
    get_data_from_influx,
    validate_time_search_format,
    get_alert_type,
    get_data_to_persist,
    process,
    get_alerts_by_criteria,
    send_alerts,
)
from challenge_app.models import Alerts
from django.db.utils import IntegrityError


class MyAppTests(TestCase):

    @patch("challenge_app.repository.influx_repo.get_client")
    @patch("challenge_app.repository.influx_repo.get_query")
    @patch("challenge_app.repository.influx_repo.get")
    def test_get_data_from_influx(self, mock_get, mock_get_query, mock_get_client):
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        mock_query = "some_query"
        mock_get_query.return_value = mock_query
        mock_data = [{"time": "2023-06-27T00:00:00Z", "value": 123}]
        mock_get.return_value = mock_data

        result = get_data_from_influx(1, "-1h")

        mock_get_client.assert_called_once()
        mock_get_query.assert_called_once_with(1, "-1h")
        mock_get.assert_called_once_with(mock_client, mock_query)
        self.assertEqual(result, mock_data)

    def test_validate_time_search_format(self):
        self.assertTrue(validate_time_search_format("-1h"))
        self.assertFalse(validate_time_search_format("1hour"))

    def test_get_alert_type(self):
        self.assertEqual(get_alert_type(1, 250), "BAJA")
        self.assertEqual(get_alert_type(1, 600), "MEDIA")
        self.assertEqual(get_alert_type(1, 900), "ALTA")
        with self.assertRaises(ValueError):
            get_alert_type(1, 100)

        self.assertEqual(get_alert_type(2, 150), "BAJA")
        self.assertEqual(get_alert_type(2, 300), "MEDIA")
        self.assertEqual(get_alert_type(2, 600), "ALTA")
        with self.assertRaises(ValueError):
            get_alert_type(2, 1000)

    @patch("challenge_app.repository.get_alert_type")
    def test_get_data_to_persist(self, mock_get_alert_type):
        mock_get_alert_type.side_effect = ["BAJA", "MEDIA", "ALTA"]
        data = [
            {"time": "2023-06-27T00:00:00Z", "value": 250},
            {"time": "2023-06-27T01:00:00Z", "value": 600},
            {"time": "2023-06-27T02:00:00Z", "value": 900},
        ]
        expected_result = [
            {
                "datetime": "2023-06-27T00:00:00Z",
                "type": "BAJA",
                "version": 1,
                "value": 250,
            },
            {
                "datetime": "2023-06-27T01:00:00Z",
                "type": "MEDIA",
                "version": 1,
                "value": 600,
            },
            {
                "datetime": "2023-06-27T02:00:00Z",
                "type": "ALTA",
                "version": 1,
                "value": 900,
            },
        ]

        result = get_data_to_persist(1, data)

        self.assertEqual(result, expected_result)

    @patch("challenge_app.service.get_data_from_influx")
    @patch("challenge_app.service.get_data_to_persist")
    @patch("challenge_app.models.Alerts.objects.create")
    def test_process(
        self, mock_create, mock_get_data_to_persist, mock_get_data_from_influx
    ):
        mock_get_data_from_influx.return_value = [
            {"time": "2023-06-27T00:00:00Z", "value": 250},
            {"time": "2023-06-27T01:00:00Z", "value": 600},
        ]
        mock_get_data_to_persist.return_value = [
            {
                "datetime": "2023-06-27T00:00:00Z",
                "type": "BAJA",
                "version": 1,
                "value": 250,
            },
            {
                "datetime": "2023-06-27T01:00:00Z",
                "type": "MEDIA",
                "version": 1,
                "value": 600,
            },
        ]

        process(1, "-1h")

        self.assertTrue(mock_create.called)

    @patch("challenge_app.models.Alerts.objects.filter")
    def test_get_alerts_by_criteria(self, mock_filter):
        mock_alert = MagicMock()
        mock_alert.datetime.strftime.return_value = "2023-06-27 00:00:00"
        mock_alert.value = 250
        mock_alert.version = 1
        mock_alert.type = "BAJA"
        mock_alert.sended = False
        mock_filter.return_value = [mock_alert]

        result = get_alerts_by_criteria(1, "BAJA", False)

        expected_result = [
            {
                "datetime": "2023-06-27 00:00:00",
                "value": 250,
                "version": 1,
                "type": "BAJA",
                "sended": False,
            }
        ]

        self.assertEqual(result, expected_result)

    @patch("challenge_app.models.Alerts.objects.filter")
    def test_send_alerts(self, mock_filter):
        mock_qs = MagicMock()
        mock_filter.return_value = mock_qs

        send_alerts(1, "BAJA")

        mock_qs.update.assert_called_once_with(sended=True)
