
// assingning variables to HTML elements

const taskInput = document.getElementById('taskInput');
const addTaskBtn = document.getElementById('addTaskButton');
const taskList = document.getElementById('taskList');
const delAllBtn = document.getElementById('deleteAllBtn');
const removeCompleteBtn = document.getElementById('removeComplete');


// Add task button functionality

addTaskBtn.addEventListener('click', function() {
    // check if input is empty
    const taskText = taskInput.value.trim();
    if (taskText === '') {
        alert('Please enter a task.');
        return;
    }

    // Create a new list item for the task
    // and append it to the task list

    const li = document.createElement('li');
    li.textContent = taskText;

    // A line through completed task

    li.addEventListener('click', function() {
        li.classList.toggle('completed');
    });

    // delete task button

    const delBtn = document.createElement('button');
    delBtn.textContent = 'Delete';
    delBtn.addEventListener('click', function() {
        taskList.removeChild(li);
    });

    li.appendChild(delBtn);
    taskList.appendChild(li);
    taskInput.value = '';
});

// Delete all tasks

delAllBtn.addEventListener('click', function() {
    while (taskList.firstChild) {
        taskList.removeChild(taskList.firstChild);
    }
});

// Remove completed tasks

removeCompleteBtn.addEventListener('click', function() {
    const completedTasks = taskList.querySelectorAll('.completed');
    completedTasks.forEach(function(task) {
        taskList.removeChild(task);
    });
});

// Allow adding task with Enter key

taskInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        addTaskBtn.click();
    }
});

