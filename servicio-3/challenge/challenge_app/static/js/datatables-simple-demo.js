window.addEventListener('DOMContentLoaded', event => {
    
    // on load
    const versionInput = document.getElementById('versionForSearch');
    
    const datatablesSimple = document.getElementById('datatablesAlerts');
    const dataTable = new simpleDatatables.DataTable(datatablesSimple);
    fetch('/challenge/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ version: versionInput.value }),
    })
    .then(response => response.json())
    .then(data => {
        let finalData = {
            data: []
        }
        data.forEach(d => {
            finalData.data.push(
                [
                    d.datetime, 
                    d.value, 
                    d.version,
                    d.type, 
                    d.sended
                ]
            )
        });
        dataTable.insert(finalData);
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    // on searchBtn is clicked

    const btnSearch = document.getElementById("btnSearch");
    btnSearch.addEventListener('click', () =>{
        const typeInput = document.getElementById("type")
        const sendedInput = document.getElementById("sended")
        let data = { version: versionInput.value };

        if (sendedInput.value !== ''){
            sendedValue = true ? sendedInput.value === "true" : false;
            data["sended"] = sendedValue;
        }
        if (typeInput.value !== ''){
            data["type"] = typeInput.value;
        }
        
        fetch('/challenge/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => {
            let finalData = {
                data: []
            }
            dataTable.destroy();
            dataTable.init();
            data.forEach(d => {
                finalData.data.push(
                    [
                        d.datetime, 
                        d.value, 
                        d.version,
                        d.type, 
                        d.sended
                    ]
                )
            });
            dataTable.insert(finalData);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    })
    
    // on btnProcess clicked
    const btnProcess = document.getElementById("btnProcess");
    btnProcess.addEventListener('click', () =>{
        const versionInput = document.getElementById('versionForProcess');
        const timeInput = document.getElementById("timeInput")
    
        let data = { version: versionInput.value };

        if (timeInput.value !== ''){
            data["timeSearch"] = timeInput.value;
        }
        else{
            alert("El campo Time es obligatorio para procesar la data");
            return;
        }
        
        fetch('/challenge/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(response => {
            if (response.status != 'ok'){
                alert(response.status);
                return
            }
            alert("Procesado ok");
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    })

    // on btnSend clicked
    const btnSend = document.getElementById("btnSend");
    btnSend.addEventListener('click', () =>{
        const versionInput = document.getElementById('versionForSend');
        const typeInput = document.getElementById("typeForSend")
    
        let data = { 
            version: versionInput.value,
            type: typeInput.value
        };
        
        fetch('/challenge/send', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            if (data.status != 'ok'){
                alert(response.status);
                return
            }
            alert("Procesado ok");
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    })
    
});
