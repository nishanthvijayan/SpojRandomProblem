var buttons = require('sdk/ui/button/action');
var tabs = require("sdk/tabs");
var xhr = require("sdk/net/xhr");
var panels = require("sdk/panel");
var self = require("sdk/self");

var res;
var req;
var problemurl;


var panel = panels.Panel({
  width: 101,
  height: 101,
  contentURL: self.data.url("spinner.html"),
});


var button = buttons.ActionButton({
  id: "spoj-link",
  label: "Visit Random Question on Spoj.com",
  icon: {
    "16": "./icon32.png",
    "32": "./icon32.png",
    "48": "./icon32.png",
    "64": "./icon32.png",
    "128":"./icon128.png"
  },
  onClick: fetchdata  
})

function fetchdata(){
  
  panel.show({ position: button });

  req =  new xhr.XMLHttpRequest();
  req.open("GET",'http://spojrandomproblemapi.herokuapp.com/',true);
  req.send();
  req.onload = function(){
  res = JSON.parse(req.responseText);
  problemurl = "http://www.spoj.com/problems/" + res.RandomProblemCode.Code;
  panel.hide();
  tabs.open(problemurl);
  };

}

