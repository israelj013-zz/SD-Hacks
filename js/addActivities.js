let activities = []
add = document.getElementById('add');

class Activity{
    constructor(activity,hour, mins){
        this.activity = activity;
        this.length = new TimeLength(hour,mins);
    }
}

class TimeLength{
    constructor(hour, mins){
        this.hour = hour;
        this.mins = mins;
        
    }
}

add.addEventListener('click', () => {
    let hour = parseInt(document.getElementById("selectHour").value);
    let mins = document.getElementsByClassName("selectMins");
    let min = parseInt(mins[0].value)*10+ parseInt(mins[1].value)
    let activity = document.getElementById('activity').value;
    let list = document.getElementById('activities');
    console.log(activity);

    if (hour != NaN && min != NaN && activity != "" && activities.length == 0){
        activities.push(new Activity(activity, new TimeLength(hour, min)));
        list.innerHTML = `<li class="list-group-item"><span>`+activity+`</span>;
                        <span style="float: right;">`+ hour+`:`+min+`</span></li>`;
    }
    else if(hour != NaN && min != NaN && activity != "" && activities.length > 0){
        activities.push(new Activity(activity, new TimeLength(hour, min)));
        list.innerHTML += `<li class="list-group-item"><span class="hour">`+activity+`</span>
                        <span class="min" style="float: right;">`+hour+`:`+min+`</span></li>`;
    }
    if (activities.length == 5){
        list.style.overflow = 'hidden';
        list.style.overflowY = 'scroll';
        list.style.height = '200px';
    }
});