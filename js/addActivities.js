let activities = []
add = document.getElementById('add');

class Activity{
    constructor(element,activity,hour, mins){
        this.element = element;
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
    let hourE = parseInt(document.getElementById("selectHour").value);
    let hour = hour;
    let mins = document.getElementsByClassName("selectMins");
    let min = parseInt(mins[0].value)*10+ parseInt(mins[1].value);
    let activity = document.getElementById('activity').value;
    let list = document.getElementById('activities');
    let errorActivity = document.getElementById('error-activity');

    if (hour != NaN || min != NaN || activity != "" || activities.length == 0){
        errorActivity.style.display = 'block';
    }

    if (hour != NaN && min != NaN && activity != "" && activities.length == 0){
        errorActivity.style.display = 'none';
        list.innerHTML = `<li class="list-group-item"><span>`+activity+`</span>
                        <span style="float: right;">`+ hour+`:`+min+`</span></li>`;
        let lists = list.getElementsByClassName('list-group-item');
        activities.push(new Activity(lists[0],activity, new TimeLength(hour, min)));
        clearForm(activity, hour, )
    }
    else if(hour != NaN && min != NaN && activity != "" && activities.length > 0){
        errorActivity.style.display = 'none';
        list.innerHTML += `<li class="list-group-item"><span class="hour">`+activity+`</span>
                        <span class="min" style="float: right;">`+hour+`:`+min+`</span></li>`;
        let lists = list.getElementsByClassName('list-group-item');
        activities.push(new Activity(lists[lists.length-1],activity, new TimeLength(hour, min)));
    }
    if (activities.length == 5){
        list.style.overflow = 'hidden';
        list.style.overflowY = 'scroll';
        list.style.height = '200px';
    }
});

function clearForm(activity, hour, min){

}