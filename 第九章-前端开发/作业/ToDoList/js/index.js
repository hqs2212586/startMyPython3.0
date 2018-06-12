/*
作为 Web Storage API 的接口，Storage 提供了访问特定域名下的会话存储（session storage）或本地存储（local storage）的功能
getItem() 作为 Storage 接口的方法，接受一个键名（key name）作为参数，并返回对应键名的值（key's value）
*/

// 所有事项（包含todo事项和done事项）
var collection = localStorage.getItem("todo");
// console.log(collection);   // [{"title":"asdadw","done":true},{"title":"aadw","done":false}]

// 添加ToDo
// 表单 输入todolist
function postaction(){
	var title = document.getElementById("title");
	// title作为对象

	// value 属性可设置或返回单选按钮的 value 属性的值
	if(title.value == "") {
		alert("内容不能为空");
	}else{

		var data= loadData();  // 输入内容json解析

		// 添加进todo事项的，"done":false
		var todo={"title":title.value,"done":false};
		// push()向数组的末尾添加一个或多个元素，并返回新的长度
		data.push(todo);
		// 转换data为JSON字符串
		saveData(data);

		// getElementById方法会使用指定的标签名返回所有的元素（作为一个节点列表）
		var form=document.getElementById("form");

		// form.reset 方法可以重置一个表单内的所有表单控件的值到初始状态
		form.reset();
		
		load();
	}
}


// 将用户输入内容进行json字符串解析
function loadData(){
	// 一个 Storage 可被用于访问当前远端（ origin ）的本地存储空间的对象
	var collection=localStorage.getItem("todo");
	if (collection!=null) {
	    //JSON.parse() 方法用来解析JSON字符串，构造由字符串描述的JavaScript值或对象。
		return JSON.parse(collection);
	}
	else return [];
}


// 将数组转化为json格式
function saveData(data){
    // storage.setItem()方法，接受一个键名和值作为参数，将会把键名添加到存储中
    // JSON.stringify() 方法是将一个JavaScript值(对象或者数组)转换为一个 JSON字符串
	localStorage.setItem("todo",JSON.stringify(data));
}

// 加载待办和完成事项
function load() {
    // todo列表：ol的内容
    var todolist = document.getElementById("todolist");
    // done列表：ul的内容
    var donelist = document.getElementById("donelist");
    var collection=localStorage.getItem("todo");

    if (collection!=null) {
        //解析json字符串为javascript值
        // console.log(collection);

        var data = JSON.parse(collection);

        var todoCount = 0;
        var doneCount = 0;
        var todoString= "";   //正在进行
        var doneString= "";   //已经完成
        for (var i = data.length - 1; i >= 0; i--) {
            if (data[i].done) {
                /*
                <li draggable="true">
                    <input type="checkbox" onchange="update(1,&quot;done&quot;,true)">
                    <p id="p-1" onclick="edit(1)">asdw</p>
                    <a href="javascript:remove(1)">-</a>
                </li>
                 */
                doneString+=
                    // draggable属性规定元素是否可拖动
                    "<li draggable='true'>" +
                        "<input type='checkbox' onchange='update("+i+",\"done\",false)' checked='checked' />" +
				        "<p id='p-"+i+"' onclick='edit("+i+")'>"+data[i].title+"</p>" +
				        "<a href='javascript:remove("+i+")'>-</a>" +
                    "</li>";
                doneCount++;
            } else {
                /*
                <li draggable="true">
                    <input type="checkbox" onchange="update(0,&quot;done&quot;,false)" checked="checked">
                    <p id="p-0" onclick="edit(0)">asd w </p>
                    <a href="javascript:remove(0)">-</a>
                </li>
                 */
                todoString+=
                    // draggable属性规定元素是否可拖动
                    "<li draggable='true'>" +
                        "<input type='checkbox' onchange='update("+i+",\"done\",false)' checked='checked' />" +
                        "<p id='p-" +i+ "' onclick='edit("+i+")'>"+data[i].title+"</p>" +
                        "<a href='javascript:remove("+i+")'>-</a>" +
                    "</li>";
                todoCount++;
            }
        };
        //innerHtml既可以识别纯文本，也可以识别标签
        // 设置内容
        todocount.innerHTML=todoCount;
		todolist.innerHTML=todoString;

		donecount.innerHTML=doneCount;
		donelist.innerHTML=doneString;
    } else {   // 如果collection为空,即没有任何事项记录，清空todo和done的事项的数量和列表
        todocount.innerHTML = 0;
        todolist.innerHTML="";
        donecount.innerHTML = 0;
        donelist.innerHTML="";
    }
    
    var lis=todolist.querySelectorAll('ol li');  // 后代选择器

    // forEach方法对数组的每个元素执行一次提供的函数
    [].forEach.call(lis,function(li) {

        // addEventListener()方法用于向指定元素添加事件句柄
        li.addEventListener('dragstart', handleDragStart,false);
        li.addEventListener('dragover', handleDragOver,false);
        li.addEventListener('drop',handleDrop,false);

        //鼠标移开时执行(只要移动一次鼠标就会遍历列表就会更新保存数据)
        onmouseout = function () {
            saveSort();
        }
    })
}

function handleDragStart(e) {
    dragSrcEl = this;
    // 在进行拖放操作时，DataTransfer 对象用来保存，通过拖放动作，拖动到浏览器的数据。
    e.dataTransfer.effectAllowed = 'move';
    e.dataTransfer.setData('text/html', this.innerHTML);
}

function handleDragOver(e) {
    // preventDefault()方法 取消事件的默认动作
    if (e.preventDefault) {
        e.preventDefault();
    }
    e.dataTransfer.dropEffect = 'move';
    return false;
}

function handleDrop(e) {
    //stopPropagation阻止捕获和冒泡阶段中当前事件的进一步传播
    if (e.stopPropagation) {
        e.stopPropagation();
    }
    if (dragSrcEl != this) {
        dragSrcEl.innerHTML = this.innerHTML;
        this.innerHTML = e.dataTransfer.getData('text/html');
    }
    return false;
}

// 保存数据
function saveSort() {
    var todolist = document.getElementById("todolist"); // <ol id="todolist" class="demo-box">
    var donelist = document.getElementById("donelist");
    var ts = todolist.getElementsByTagName("p");
    var ds = donelist.getElementsByTagName("p");
    var data = [];
    // 遍历todo列表事项
    for (i=0;i<ts.length;i++) {
        // 即将todo的事项
        var todo = {
            "title":ts[i].innerHTML,"done":false
        };
        // unshift()方法可向数组的开头添加一个或更多元素，并返回新的长度.
        data.unshift(todo);
        /*  data里的内容：如果有内容会从0开始，依次添加进去
        0:{title: "阿斯达多", done: false}
        1:{title: "大", done: false}
         */
    }
    // 遍历done列表事项
    for (i=0;i<ds.length;i++) {
        // 已经done的事项
        var todo = {
            "title":ds[i].innerHTML,"done":true
        };
        data.unshift(todo);
    }
    saveData(data);
}


// onclick 事件会在对象被点击时发生：针对<p id="p-0" onclick="edit(0)">大萨达</p>
function edit(i) {
	load();
	// 匹配特定ID值的元素：id="p-"+i
	var p = document.getElementById("p-"+i);
	title = p.innerHTML;
	// console.log(title);   // 撒大声地 （标签里的内容）

	p.innerHTML="<input id='input-"+i+"' value='"+title+"' />";
	var input = document.getElementById("input-"+i);

	/*
	setSelectionRange 方法可以从一个被 focused 的 <input> 元素中选中特定范围的内容
	selectionStart:被选中的第一个字符的位置  0
	selectionEnd:被选中的最后一个字符的下一个位置   input.value.length
	 */
	input.setSelectionRange(0,input.value.length);

	/* CSS伪类：Selects any <input> when focused
	input:focus {
        outline-width: 0;
    }
	 */
	input.focus();
	input.onblur = function(){
		if(input.value.length == 0){
			p.innerHTML = title;
			alert("内容不能为空");
		}
		else{
			update(i,"title",input.value);
		}
	};
}

// 一张页面或一幅图像完成加载
window.onload=load;
// 用于向指定元素添加事件句柄
window.addEventListener("storage",load,false);

var dragSrcEl = null;

/*
修改todolist和donelist中<p id="p-1" onclick="edit(1)">asdw</p>的内容
 */
function update(i,field,value){
    // 首先加载进了所有todo事项和done事项列表
	var data = loadData();

	// splice() 方法用于插入、删除或替换数组的元素
	// 从第i位开始删除1个元素,要删除这个元素的内容
    var todo = data.splice(i,1)[0];
    // console.log(todo);
    // {title: "撒大声地", done: false}


	todo[field] = value;  //filed='title'
	// 在data数组中第i位加入todo的新值，不删除
	data.splice(i,0,todo);
	saveData(data);
	load();
}

/* 从列表中删除
   从done列表和todo列表点击"-"符号，都是直接删除记录
 */
// load函数在创建DOM标签的时候，<a href="javascript:remove(0)">-</a>
function remove(i){
    // 首先加载进了所有todo事项和done事项列表
	var data = loadData();

	// splice()方法用于插入、删除或替换数组的元素，会直接改变原数组
    // 从第i位（从0开始排序和<a>标签里remove(i)编号一致）删除一个元素
	var todo = data.splice(i,1)[0];

	saveData(data);
	load();
}


// clear清空
// clear() 是 Storage 接口的一个方法，调用它可以清空存储对象里所有的键值
function clear(){
	localStorage.clear();
	load();
}