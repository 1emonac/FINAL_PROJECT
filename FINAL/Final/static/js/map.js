let lat = 37.566826
let lng = 126.9786567

function getSuccess(position) {
    lat = position.coords.latitude;// 위도
    lng = position.coords.longitude;// 경도
    
    
    const accuracy = Math.floor(position.coords.accuracy); // 위도 경도 오차(m)

    var mapContainer = document.getElementById('map'), // 지도를 표시할 div  
    mapOption = { 
        center: new kakao.maps.LatLng(lat,lng), // 지도의 중심좌표
        level: 5 // 지도의 확대 레벨
    };

    var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다
    fetchPy(sleep_clinic, lat, lng)
}

function fetchPy(keyword, lat, lng) {
    const csrftoken = document.querySelector('input[name=csrfmiddlewaretoken]').value;
    console.log(csrftoken);
    fetch("/sleep/clinic/", {
        method: "POST",
        headers:{
            Accept: "application / json", 
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({
            "x" : lng,
            "y" : lat,
        })
    }).then(res => res.text())
    .then(data => {         

        sleep_clinic = JSON.parse(data).sleep_clinic
        
        var mapContainer = document.getElementById('map'), // 지도를 표시할 div  
        mapOption = { 
            center: new kakao.maps.LatLng(lat,lng), // 지도의 중심좌표
            level: 5 // 지도의 확대 레벨
        };

        var map = new kakao.maps.Map(mapContainer, mapOption);


        var positions = []
        switch (keyword) {
            case "sleep_clinic":
                
                break;
        
            default:
                break;
        }

        sleep_clinic.map(e => {
            var object = new Object();
            object.latlng =new kakao.maps.LatLng(e.y, e.x)
            positions.push(object)
        })

        
        for (var i = 0; i < positions.length; i ++) {
            // 마커를 생성합니다
            var marker = new kakao.maps.Marker({
                map: map, // 마커를 표시할 지도
                position: positions[i].latlng // 마커의 위치
            });
        }

        // 리스트 생성
        for ( var i = 0; i < sleep_clinic.length; i++ ) {
            var listEl = document.getElementById('placesList'),
            fragment = document.createDocumentFragment(); 
            var placePosition = new kakao.maps.LatLng(sleep_clinic[i].y, sleep_clinic[i].x),
                itemEl = getListItem(i, sleep_clinic[i]); // 검색 결과 항목 Element를 생성합니다
          
            fragment.appendChild(itemEl);
            listEl.appendChild(fragment);
            }
            
             // 검색결과 항목들을 검색결과 목록 Element에 추가합니다
        
        
        

    })
}

function getError() {
    var mapContainer = document.getElementById('map'), // 지도를 표시할 div  
    mapOption = { 
        center: new kakao.maps.LatLng(lat,lng), // 지도의 중심좌표
        level: 5 // 지도의 확대 레벨
    };

    var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다
    map
}

navigator.geolocation.getCurrentPosition(getSuccess, getError); 
// 장소 받아오기 -> 성공시 getSuccess, 실패시 getError 함수사용//

//-----------------------------------------------------------------성공라인//





function getListItem(index, places) {

        var el = document.createElement('li'),
        itemStr = '<span class="markerbg marker_' + (index+1) + '"></span>' +
                    '<div class="info">' +
                    '   <h5>' + places.place_name + '</h5>';

        if (places.road_address_name) {
            itemStr += '    <span>' + places.road_address_name + '</span>' +
                        '   <span class="jibun gray">' +  places.address_name  + '</span>';
        } else {
            itemStr += '    <span>' +  places.address_name  + '</span>'; 
        }
                    
        itemStr += '  <span class="tel">' + places.phone  + '</span>' +
                    '</div>';           

        el.innerHTML = itemStr;
        el.className = 'item';

        return el;
        }

