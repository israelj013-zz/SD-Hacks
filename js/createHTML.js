function createHours(){
    dropdown = document.getElementById("selectHour");
    dropdown.innerHTML = addOptions(10);
}

function createMinutes(){
    dropdown = document.getElementsByClassName("selectMinutes");
    dropdown[0].innerHTML = addOptions(6);
    dropdown[1].innerHTML = addOptions(10);
}

function createDays(){
    dropdown = document.getElementById('selectDay');
    const days = ['Mon','Tues','Wed','Thurs','Fri']
    let options = `<option>Select</option>`
    for (var day=0;day<days.length;day++){
        options += `<option>`+days[day]+`</option>`
    }
    dropdown.innerHTML = options
}

function addOptions(num){
    let options = `<option>Select</option>`;
    for (var i=0;i<num;i++){
        options += `<option>`+i+`</option>`
    }
    return options
}



createDays();
createHours();
createMinutes();