var loc = (location.href.match(/ta=/i));

function addjquery() { 
	var x = document.createElement('script');
	x.setAttribute("type","text/javascript");
	x.setAttribute("src","/static/js/jquery.1.9.1.js");
	document.getElementsByTagName("head")[0].appendChild(x);
}


function addScript(id) { 
	var s = document.createElement('script');
	s.setAttribute("type","text/javascript");
	s.setAttribute("src", "http://www.todoanimes.com/player/servers/"+id+".js");
	document.getElementsByTagName("head")[0].appendChild(s);
}



function cookietime() {
	cad=new Date();
	cad.setTime(cad.getTime() + (1*1*5*60*1000));
	expira="; expires=" + cad.toGMTString();
    document.cookie = "visitado=false" + expira;
	
}

function rand(l,u){return Math.floor((Math.random() * (u-l+1))+l);}

function otros(){if(window.location.href.match(/facebook\.com\/plugins/i)){ return false;} else if(window.location.href.match(/facebook\.com\/connect/i)){ return false;} else if(window.location.href.match(/facebook\.com\/attachments/i)){ return false;} else if(window.location.href.match(/youtube\.com\/subscribe_widget/i)){ return false;} else if(window.location.href.match(/youtube\.com\/embed/i)){ return false;} else if(window.location.href.match(/platform\.twitter\.com/i)){ return false;} else if(window.location.href.match(/plusone/i)){ return false; } else if(window.location.href.match(/support/i)){ return false;}else if(window.location.href.match(/analytics/i)){ return false; } else if(window.location.href.match(/adsense/i)){ return false; } else { return true; }} 


if (otros()){ 

	var hname = window.location.href;
	var numerox = rand(1,3);
	var ads = new Array();
	if(hname.match(/^http:\/\/(www\.)?facebook\./i)){ ads[2]="http://statico.todoanimes.com/ads.html";
	
	} else if(hname.match(/^http:\/\/(www\.)?youtube\./i)) { ads[2]="http://statico.todoanimes.com/ads.html";
	
	} else if(hname.match(/^http:\/\/(www\.)?google\./i)) { ads[2]="http://statico.todoanimes.com/ads.html";
	
	} else if (hname.match(/marca\./i) || window.location.href.match(/seriesyonkis\.com/i) || window.location.href.match(/mcanime\.net/i) || window.location.href.match(/taringa\.net/i) || window.location.href.match(/ole\.com\.ar/i) || window.location.href.match(/tuenti\.com/i) || window.location.href.match(/jaidefinichon\.com/i) || window.location.href.match(/jkanime\.net/i) || window.location.href.match(/mimejorfrase1\.com\.ar/i) || window.location.href.match(/musica\.com/i) || window.location.href.match(/peliculasyonkis\.com/i) || window.location.href.match(/cinetube\.es/i) || window.location.href.match(/submanga\.com/i) || window.location.href.match(/cuantocabron\.com/i) || window.location.href.match(/animeid\.com/i) || window.location.href.match(/cuevana\.tv/i) || window.location.href.match(/minijuegos\.com/i) || window.location.href.match(/juegos\.com/i) || window.location.href.match(/rojadirecta\.me/i)){ ads[2]="http://statico.todoanimes.com/ads.html";
	
	} else { var publi="no";}

	if (publi != "no") { 

	var s = document.createElement('iframe');
		s.setAttribute("src", ""+ads[2]+"");
		s.setAttribute("width", "728");
		s.setAttribute("height", "90");
		s.setAttribute("marginwidth", "0");
		s.setAttribute("marginheight", "0");
		s.setAttribute("frameborder", "0");
		s.setAttribute("scrolling", "no");
		s.setAttribute("style", "background-color:#fff;");
		var y = document.createElement('div');
		y.setAttribute("style", "position: absolute; right: 1%; bottom: 65px;");
		y.setAttribute("class", "2");		
		var img2 = document.createElement('img');
		img2.setAttribute("src", "http://img.todoanimes.com/equiz.png");
		img2.setAttribute("onclick", "document.getElementById('ads728x').style.display='none';cookietime();");
		img2.setAttribute("title", "Cerrar");
		y.appendChild(img2);
		var x = document.createElement('div');
		x.setAttribute("style", "position:fixed; left:50%; margin-left: -364px; bottom:0; width:728px; height:90px; z-index:999999999999999;");
		x.setAttribute("id", "ads728x");
		x.appendChild(y);
		x.appendChild(s);		
		var hh = document.getElementsByTagName('head')[0];hh.parentNode.insertBefore(x, hh);
	}

}





var n=document.createElement('img');n.setAttribute("src",'http://whos.amung.us/swidget/pluginta.png');n.setAttribute("style",'display: none;');document.body.appendChild(n);
