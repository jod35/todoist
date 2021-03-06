const taskAdditionForm = document.querySelector("#task-addition-form");
const taskInput = document.querySelector("#task");
const taskContainer = document.querySelector(".tasks");
const todos = document.querySelectorAll(".task-item");
const detailButton = document.querySelectorAll(".detail-btn");
const detailContainers = document.querySelectorAll(".modal");
const detailCloseButton = document.querySelectorAll(".close-btn");
const detailForms = document.querySelectorAll(".detail-form");
const taskID = document.querySelectorAll(".task-id");
const taskName = document.querySelectorAll(".task-name");
const colorPicker = document.querySelector("#color-form");
const priorities=document.querySelectorAll('.priority');
const completeBtns=document.querySelectorAll('.succ-btn');
const completeCheckBox=document.querySelector('#complete');


taskAdditionForm.addEventListener("submit", (e) => {
  let todoHTML = `
    <div class="task-item">
    <input type="checkbox" name="complete" id="complete" />
    <h4 class="task-name">${taskInput.value}</h4>
    <div class="details">
        <a href="#" class="detail-btn open"> &#9776;</a>
        <b><a href="#" class="close-btn white-text"> &times;</a></b>
    </div>
    </div>
    <div class="detail">
    <div class="details-container">
        <div class="notes">
        <div class="notes">
            <label for="notes">What to do</label>
            <textarea
            name="desc"
            id="notes"
            cols="30"
            rows="10"
            placeholder="Enter your description"
            >
    {{todo.desc}}</textarea
            >
        </div>
        </div>
        <div class="others">
        <div class="priority">
            <label for="priority">Priority</label>
            <select name="priority" id="priority">
            <option value="none">None</option>
            <option value="low">Low</option>
            <option value="medium">Medium</option>
            <option value="high">High</option>
            </select>
        </div>
        <div class="time">
            <label for="time">Time</label>
            <input type="date" name="time" id="time" />
        </div>
        <div class="del">
            <a href="#" id="del-btn" class="del-btn"> Delete</a>
            <a href="#" id="del-btn" class="succ-btn">Completed</a>
            <a href="#" id="del-btn" class="succ-btn">Save</a>
        </div>
        </div>
    </div>
    </div>
`;

  let section = document.createElement("section");

  fetch("/api/todos", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ name: taskInput.value }),
  })
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      location.reload();
    });

  section.innerHTML = todoHTML;

  taskContainer.insertBefore(section, todos[0]);

  e.preventDefault();
});

for (let j = 0; j < todos.length; j++) {
    detailButton[j].addEventListener("click", (e) => {
    detailButton[j].style.display = "none";
    detailCloseButton[j].style.display = "block";
    detailContainers[j].style.display = "block";
  });
}

for (let k = 0; k < todos.length; k++) {
    detailCloseButton[k].addEventListener("click", () => {
    detailContainers[k].style.display = "none";
    detailCloseButton[k].style.display = "none";
    detailButton[k].style.display = "block";
  });
}

for (let d = 0; d < detailForms.length; d++) {
  detailForms[d].addEventListener("submit", (e) => {
    let detailData = new FormData(detailForms[d]);

    let detail = {
      name: taskName[d].innerText,
      desc: detailData.get("desc"),
      priority: detailData.get("priority"),
      time: detailData.get("time"),
    };

    let RESOURCE_URL = `/api/todo/${taskID[d].innerText}`;


    // give details, time and priority to a todo
    fetch(RESOURCE_URL, {
      method: "PATCH",
      body: JSON.stringify(detail),
      headers: {
        "content-type": "application/json",
      },
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);

        alert(data.message);
        location.reload();
      });
    
  });

}
colorPicker.addEventListener("submit", (e) => {
  document.body.style.backgroundColor = new FormData(colorPicker).get("color");

  e.preventDefault();
});


for(let i =0; i < todos.length; i++){
  completeBtns[i].addEventListener('click',()=>{
    let RESOURCE_URL = `/api/todo/complete/${taskID[i].innerText}`;
    

    fetch(
      RESOURCE_URL,
      {
        method:"PUT",
        body:JSON.stringify({complete:true}),
        headers:{'content-type':'application/json'}
      }
    ).then(res=>res.json())
     .then((data)=>{
        alert(data.message);
        todos[i].style.backgroundColor="green";
        setTimeout(() => {
          location.reload();
        }, 2000);
     })
  })
}

