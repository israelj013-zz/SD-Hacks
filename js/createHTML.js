function createHours(id){
    dropdown = document.getElementById(id);
    dropdown.innerHTML = addOptions(10);
}



function createMins(){
    dropdown = document.getElementsByClassName("selectMins");
    dropdown[0].innerHTML = addOptions(6);
    dropdown[1].innerHTML = addOptions(10);
}

function addOptions(num){
    let options = `<option>Select Activity Length</option>`;
    for (var i=0;i<num;i++){
        options += `<option>`+i+`</option>`
    }
    return options
}

createHours("selectHour");
createHours("selectHourStart");
createHours("selectHourEnd");
createMins();