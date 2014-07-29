
var res;
var req;



function fetchdata(){
  
  req =  new XMLHttpRequest();
  req.open("GET",'http://spojrandomproblemapi.herokuapp.com/',true);
  req.send();
  req.onload = function(){
  res = JSON.parse(req.responseText);
  problemurl = "http://www.spoj.com/problems/" + res.RandomProblemCode.Code
  chrome.tabs.create({url: problemurl})
  };

}


$(document).ready(function(){

  fetchdata();

});

