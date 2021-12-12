async function generate_data() {
    var country_name = document.getElementById('country').value;
    if (country_name == '') {
        alert('Please enter the country name');        
    } else {
        var corona_data = await eel.get_data(country_name)();
        if (corona_data == 'Country not found!') {
            alert('Please enter the correct country name!');
        } else {
            document.getElementById('head').innerHTML = '';
            var button = document.getElementById('submit');
            button.innerHTML = 'Go Back';
            button.onclick = function() {
                window.location.replace('tutorial_4.html');
            }
            var head = document.getElementById('head');
            var p = document.createElement('h1');
            var t = document.createTextNode('Generated Results For: ' + country_name);
            var src;
            p.appendChild(t);
            head.appendChild(p);
            var table = document.createElement('table');
            table.setAttribute('class', 'center');
            for (i = 0; i < Object.entries(corona_data).length; i++) {
                var row = table.insertRow(i);
                var cell1 = row.insertCell(0);
                var cell2 = row.insertCell(1);
                for (const[key, value] of Object.entries(Object.entries(corona_data)[i][1])) {
                    if (key == 'image') {
                    	src = value;
                    } else {
                    	cell1.innerHTML = key;
                    	cell2.innerHTML = value;
                    	cell2.className = 'totals';
                    }
                }
            }
            head.appendChild(table);
            var br = document.createElement('br');
            head.appendChild(br);
            head.appendChild(br);
            
            var div = document.createElement('div');
            div.className = 'image';
            var img = document.createElement('img');
            img.src = src; <!-- 'images/' + country_name + '.png' -->
            div.appendChild(img);
            head.appendChild(div);
        }
    }
}    
function selChange(country) {
    if (country != '') {
        document.getElementById('country').value = country;
    }
}    
async function update_countries() {
    var countries = await eel.get_countries()(), i = 0;
    var selData = document.getElementById('selCountry')
    for (i = 0; i < countries.length; i++) {
        var option = document.createElement('option');
        option.value = countries[i];
        option.innerHTML = countries[i];
        selData.appendChild(option);
    }
}    
