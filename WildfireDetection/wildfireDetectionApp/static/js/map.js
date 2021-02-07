window.onload = function() {
    initMap();
    //getMarkers();
};

var map;
var discoPark = {lat: 33.2539, lng: -97.1528};
var INTERVAL = 10000;
var markerList = {};


function initMap() {
    map = new google.maps.Map(
        document.getElementById('map'), {
            center: discoPark,
            zoom: 16,
            mapTypeId: 'terrain',
            styles: [
                {
                    "featureType": "poi",
                    "elementType": "all",
                    "stylers": [
                        { "visibility": "off"}
                    ]
                }
            ],
            disableDefaultUI: true
        }
    )
};

function getMarkers() {
    $.ajax({
        type : "POST",
        url : 'wildfireDetectionApp/ajax/markers/',
        data : {
            'csrfmiddlewaretoken': '{{ csrf_token }}',
        },
        success : function(data) {
            console.log("Got markers")
        }
    });
   len = res.length;
   for(var i = 0; i < len; i++) {
       if(markerList.hasOwnProperty(res[i].id)) {
           markerList[res[i].id].setPosition(new google.maps.LatLng(res[i].latitude, res[i].longitude));
       } else {
           var marker = new google.maps.Marker({
               position: new google.maps.LatLng(res[i].latitude, res[i].longitude),
                map: map
           });
           markerList[res[i].id] = marker;
       }
   }
   window.setTimeout(getMarkers, INTERVAL)
};


// $(document).ready(function() {
//    map = new google.maps.Map(
//        document.getElementById('map'), {
//            center: discoPark,
//            zoom: 13,
//            mapTypeId: 'terrain',
//            styles: [
//                {
//                    "featureType": "poi",
//                    "elementType": "all",
//                    "stylers": [
//                        { "visibility": "off" }
//                    ]
//                }
//            ],
//            disableDefaultUI: true
//        }
//    )
//
//    function getMarkers() {
//        $.get('/markers', {}, function(res, resp) {
//            for(var i = 0; len=res.length; i < len) {
//                if(markerList.hasOwnProperty(res[i].id)) {
//                    markerList[res[i].id].setPosition(new google.maps.LatLng(res[i].latitude, res[i].longitude));
//                } else {
//                    var marker = new google.maps.Marker({
//                        position: new google.maps.LatLng(res[i].latitude, res[i].longitude),
//                         map: map
//                    });
//                    markerList[res[i].id] = marker;
//                }
//            }
//            window.setTimeout(getMarkers, INTERVAL)
//        }, "json");
//    }
// });


$(function() {
    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});