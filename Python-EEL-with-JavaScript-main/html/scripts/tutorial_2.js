async function redirect() { 
    document.body.innerHTML = '';
    let n = await eel.generate_data()();
    var div = document.createElement('div');
    div.setAttribute('class', 'output');
    document.body.appendChild(div);
    var p = document.createElement('h1');
    var t = document.createTextNode('Generated Results:');
    p.appendChild(t);
    div.appendChild(p);
    var table = document.createElement('table');
    for (i = 0; i < Object.entries(n).length; i++) {
        var row = table.insertRow(i);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        for (const[key, value] of Object.entries(Object.entries(n)[i][1])) {
            cell1.innerHTML = key;
            cell2.innerHTML = value;
        }
    }
    div.appendChild(table);
    var button = document.createElement('button');
    button.innerHTML = 'Go Back';
    button.onclick = function() {
        window.location.replace('tutorial_2.html');
    }
    var btnDiv = document.createElement('div');
    btnDiv.className = 'submit';
    document.body.appendChild(btnDiv);
    btnDiv.appendChild(button);
}    
