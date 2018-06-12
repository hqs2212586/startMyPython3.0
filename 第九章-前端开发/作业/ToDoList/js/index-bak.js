// clear清空
function clear(){
	localStorage.clear();
	load();
}

// 表单 输入todolist
function postaction(){
	var title = document.getElementById("title");
	// value 属性可设置或返回单选按钮的 value 属性的值
	if(title.value == "") {
		alert("内容不能为空");
	}else{
		var data=loadData();
		var todo={"title":title.value,"done":false};
		// push()向数组的末尾添加一个或多个元素，并返回新的长度
		data.push(todo);
		// 转换data为JSON字符串
		saveData(data);
		var form=document.getElementById("form");
		// form.reset 方法可以重置一个表单内的所有表单控件的值到初始状态
		form.reset();
		load();
	}
}

// 用户输入内容进行json字符串解析
function loadData(){
	// 一个 Storage 可被用于访问当前远端（ origin ）的本地存储空间的对象
	var collection=localStorage.getItem("todo");
	if(collection!=null){
	    //JSON.parse() 方法用来解析JSON字符串，构造由字符串描述的JavaScript值或对象。
		return JSON.parse(collection);
	}
	else return [];
}


function saveSort(){
	var todolist=document.getElementById("todolist");
	var donelist=document.getElementById("donelist");
	var ts=todolist.getElementsByTagName("p");
	var ds=donelist.getElementsByTagName("p");
	var data=[];
	for(i=0;i<ts.length; i++){
		var todo={"title":ts[i].innerHTML,"done":false};
		// unshift()方法可向数组的开头添加一个或更多元素，并返回新的长度
		data.unshift(todo);
	}
	for(i=0;i<ds.length; i++){
		var todo={"title":ds[i].innerHTML,"done":true};
		data.unshift(todo);
	}
	// 转换data为JSON字符串
	saveData(data);
}

// JavaScript值(对象或者数组)转换为一个 JSON字符串
function saveData(data){
    // JSON.stringify() 方法是将一个JavaScript值(对象或者数组)转换为一个 JSON字符串
	localStorage.setItem("todo",JSON.stringify(data));
}

function remove(i){
    // loadData将用户输入进行json字符串解析
	var data=loadData();
	//
	var todo=data.splice(i,1)[0];
	saveData(data);
	load();
}

function update(i,field,value){
    // loadData将数据解析为数组
	var data = loadData();
	// splice() 方法用于插入、删除或替换数组的元素
	// 从第i位开始删除1个元素,要删除这个元素的内容
    var todo = data.splice(i,1)[0];
	todo[field] = value;
	// 在data数组中第i位加入todo的新值，不删除
	data.splice(i,0,todo);
	saveData(data);
	load();
}

function edit(i)
{
	load();
	var p = document.getElementById("p-"+i);
	title = p.innerHTML;
	p.innerHTML="<input id='input-"+i+"' value='"+title+"' />";
	var input = document.getElementById("input-"+i);
	input.setSelectionRange(0,input.value.length);
	input.focus();
	input.onblur =function(){
		if(input.value.length == 0){
			p.innerHTML = title;
			alert("内容不能为空");
		}
		else{
			update(i,"title",input.value);
		}
	};
}


function load(){
	var todolist=document.getElementById("todolist");
	var donelist=document.getElementById("donelist");
	var collection=localStorage.getItem("todo");
	if(collection!=null){
	    // JSON.parse() 方法用来解析JSON字符串
		var data=JSON.parse(collection);
		var todoCount=0;
		var doneCount=0;
		var todoString="";  //正在进行
		var doneString="";  //已经完成
		for (var i = data.length - 1; i >= 0; i--) {
			if(data[i].done){
				doneString+="<li draggable='true'><input type='checkbox' onchange='update("+i+",\"done\",false)' checked='checked' />"
				+"<p id='p-"+i+"' onclick='edit("+i+")'>"+data[i].title+"</p>"
				+"<a href='javascript:remove("+i+")'>-</a></li>";
				doneCount++;
			}
			else{
				todoString+="<li draggable='true'><input type='checkbox' onchange='update("+i+",\"done\",true)' />"
				+"<p id='p-"+i+"' onclick='edit("+i+")'>"+data[i].title+"</p>"
				+"<a href='javascript:remove("+i+")'>-</a></li>";
				todoCount++;
			}
		};

		// innerHtml来识别标签（也可以识别文本）
		todocount.innerHTML=todoCount;
		todolist.innerHTML=todoString;

		donecount.innerHTML=doneCount;
		donelist.innerHTML=doneString;
	}
	else{
		todocount.innerHTML=0;
		todolist.innerHTML="";
		donecount.innerHTML=0;
		donelist.innerHTML="";
	}

	// querySelectorAll返回一个 NodeList 表示元素的列表，把当前的元素作为根与指定的选择器组相匹配,'ol li'是选择器
	var lis=todolist.querySelectorAll('ol li');
	[].forEach.call(lis, function(li) {
	    // addEventListener()方法用于向指定元素添加事件句柄。
        li.addEventListener('dragstart', handleDragStart, false);
		li.addEventListener('dragover', handleDragOver, false);
		li.addEventListener('drop', handleDrop, false);
        // 鼠标移出指定的对象时发生
		onmouseout =function(){
			saveSort();
		};
	});
}

// 一张页面或一幅图像完成加载
window.onload=load;
// 用于向指定元素添加事件句柄
window.addEventListener("storage",load,false);

var dragSrcEl = null;

function handleDragStart(e) {
  dragSrcEl = this;
  e.dataTransfer.effectAllowed = 'move';
  e.dataTransfer.setData('text/html', this.innerHTML);
}
function handleDragOver(e) {
  // event.preventDefault()方法 取消事件的默认动作
  if (e.preventDefault) {
    e.preventDefault();
  }
  e.dataTransfer.dropEffect = 'move';
  return false;
}
function handleDrop(e) {
  if (e.stopPropagation) {
    e.stopPropagation();
  }
  if (dragSrcEl != this) {
    dragSrcEl.innerHTML = this.innerHTML;
    this.innerHTML = e.dataTransfer.getData('text/html');
  }
  return false;
}