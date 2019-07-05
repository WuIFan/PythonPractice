var event;
event = document.createEvent('Event');
event.initEvent("keydown", true, true);
event.view = window;
event.keyCode = 13;
event.which = 13;
event.charCode = 13;
event.code = "Enter";
event.key = "Enter";
event.bubbles = true;
var ele=document.getElementById('sb_form_q');
ele.dispatchEvent(event);

//

var event;
event = document.createEvent('Event');
event.initEvent("keypress", true, true);
event.view = window;
event.keyCode = 13;
event.which = 13;
event.charCode = 13;
event.code = "Enter";
event.key = "Enter";
event.bubbles = true;

event.altkey=false;
event.shiftey=false;
event.ctrlkey=false;
event.composed=true;
event.defaultPrevented=false;
event.detail=0;
event.eventPhase=0;
event.isComposing=false;
event.location=0;
event.metaKey=false
event.repeat=false;
var ele=document.getElementById('sb_form_q');
ele.dispatchEvent(event);

//

var event;
event = document.createEvent('Event');
event.initEvent("keydown", true, true);
event.view = window;
event.keyCode = 13;
event.which = 13;
event.charCode = 0;
event.code = "Enter";
event.key = "Enter";
event.bubbles = true;

event.altkey=false;
event.shiftey=false;
event.ctrlkey=false;
event.composed=true;
event.defaultPrevented=false;
event.detail=0;
event.eventPhase=0;
event.isComposing=false;
event.location=0;
event.metaKey=false
event.repeat=false;
var ele=document.getElementById('sb_form_q');
ele.dispatchEvent(event);

//

        if(keyCode==13){
            var e = new KeyboardEvent(eventType, {
                key:keySequence.key,
                code:keySequence.code,
                charCode:charCode,
                keyCode:keyCode,
                which:which,
                bubbles:true,
                cancelable:true,
                view:window,
                composed:true,
                });
            console.log(e);
            element.dispatchEvent(e);
        }

//

var event;
event = document.createEvent('Event');
event.initEvent("submit", true, true);
event.cancelable=true;
event.defaultPrevented=true;
var ele=document.getElementById('input');
ele.dispatchEvent(event);

//

var event;
event = document.createEvent('Event');
event.initEvent("submit", true, true);
var ele=document.getElementById('input');
ele.dispatchEvent(event);

//

var event;
event = document.createEvent('Event');
event.initEvent("textInput", true, true);
event.view = window;
event.data = "f";
var ele=document.getElementById('input');
ele.dispatchEvent(event);

//Amazon

var event;
event = document.createEvent('Event');
event.initEvent('keydown', true, true);
event.view = window;
event.altKey = undefined;
event.ctrlKey = undefined;
event.shiftKey = undefined;
event.keyCode = 70;
event.which = 70;
event.charCode = 0;
event.code = "KeyF";
event.key = "f";
event.bubbles = true;
var ele=document.getElementById('twotabsearchtextbox');
ele.dispatchEvent(event);

//

(function() {
  Element.prototype._addEventListener = Element.prototype.addEventListener;
  Element.prototype.addEventListener = function(a,b,c) {
    if(c==undefined)
        c=false;
    this._addEventListener(a,b,c);
    if(!this.eventListenerList)
        this.eventListenerList = {};
    if(!this.eventListenerList[a])
        this.eventListenerList[a] = [];
    this.removeEventListener(a,b,c);
    this.eventListenerList[a].push({listener:b,useCapture:c});
  };

//

ƒ (t){
    return"undefined"!=typeof le&&le.event.triggered!==t.type?le.event.dispatch.apply(e,arguments):void 0
}

function s(e){"mouseenter"===e.type?(document.dispatchEvent(new CustomEvent("npr:dropdownOpened")),e.target.querySelectorAll(".submenu")[0].classList.add("is-expanded"),e.target.setAttribute("aria-expanded","true")):(e.target.querySelectorAll(".submenu")[0].classList.remove("is-expanded"),e.target.setAttribute("aria-expanded","false"))}
function f(){var e=document.querySelectorAll(".menu__item--has-submenu");Array.prototype.forEach.call(e,function(e){e.removeEventListener("mouseenter",s),e.removeEventListener("mouseleave",s),e.removeAttribute("aria-haspopup"),e.removeAttribute("aria-expanded")});var t=document.querySelectorAll(".npr-header .submenu.is-expanded");Array.prototype.forEach.call(t,function(e){e.classList.remove("is-expanded")})}function l(){var e=document.querySelectorAll(".npr-header .submenu.is-expanded");Array.prototype.forEach.call(e,function(e){e.classList.remove("is-expanded");var t=e.parentNode.querySelectorAll(".menu__toggle-submenu")[0];t.setAttribute("aria-expanded","false"),t.classList.remove("is-expanded")})}function d(){document.getElementsByTagName("body")[0].classList.contains("tmplEventMusicStory")?window.pageYOffset>=138?document.getElementsByTagName("body")[0].classList.add("has-fixed-standard-sponsorship"):document.getElementsByTagName("body")[0].classList.remove("has-fixed-standard-sponsorship"):document.getElementsByTagName("body")[0].classList.contains("music")||document.getElementsByTagName("body")[0].classList.contains("about")?window.pageYOffset>=100?document.getElementsByTagName("body")[0].classList.add("has-fixed-standard-sponsorship"):document.getElementsByTagName("body")[0].classList.remove("has-fixed-standard-sponsorship"):window.pageYOffset>=45?document.getElementsByTagName("body")[0].classList.add("has-fixed-standard-sponsorship"):document.getElementsByTagName("body")[0].classList.remove("has-fixed-standard-sponsorship"),window.pageYOffset>=15?document.getElementsByTagName("body")[0].classList.add("has-fixed-player"):document.getElementsByTagName("body")[0].classList.remove("has-fixed-player")}function p(){var e=new Date,t=new Date(e.getFullYear(),e.getMonth(),e.getDate()+1),n=t-e,r=n+2;return Math.round(r)}function m(){document.querySelector(".submenu__item--timed:not(.hidden)").classList.add("hidden"),y()}function y(){var e=(new Date).getDay();0===e?document.querySelector(".submenu__item--sunday").classList.remove("hidden"):6===e?document.querySelector(".submenu__item--saturday").classList.remove("hidden"):document.querySelector(".submenu__item--weekday").classList.remove("hidden"),setTimeout(m,p())}document.getElementsByTagName("body")[0].classList.contains("utility")||document.getElementsByTagName("body")[0].classList.contains("donation-portal")||(e(),y(),window.addEventListener("scroll",d),window.addEventListener("resize",_.debounce(e,300)))})}).call(t,function(){return this}(),n(160)(e))}});
https://www.barnesandnoble.com/s/abc?_requestid=1172570
https://www.barnesandnoble.com/includes/submit.jsp?_DARGS=/cartridges/HeaderSearchBox/HeaderSearchBox.jsp

//
{
    "StartPoint":
        {
            "X": 1,
            "Y": 2
        },
    "Movements":
        [
            {
                "TD": 3,
                "OX": 4,
                "OY": 5
            },
            {
                "TD": 6,
                "OX": 7,
                "OY": 8
            }
        ]
}        
        