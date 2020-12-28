const todoForm=document.querySelector('form');
const todoContainer=document.querySelector('.todos');

todoForm.addEventListener('submit',(e)=>{

    let tododata=new FormData(todoForm);

    let todo={
        name:tododata.get('name'),
        desc:tododata.get('desc')
    }

    let todoEntry=document.createElement('p');

    todoEntry.innerText=`${todo.name} ${todo.desc}`
    todoContainer.appendChild(todoEntry);

    todoEntry.classList.add("mybtn");
    
    todoForm.reset();
    
    e.preventDefault();
})