// Variaveis globais:
var map;
var layer;
var markers = [];

// Inicializando o mapa do OpenStreetMap:
function initmap(id) {

	map = new L.Map('map', getPositionOptions());

	var osmUrl = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
	layer = new L.TileLayer(osmUrl);
	map.setView(new L.LatLng(-20.297618, -40.295777), 10);
	map.addLayer(layer);

	//Atualiza os marcadores a cada x milisegundos:
	setInterval(function () {
		$.when(getData(id)).done(function (item) {
			var itens = [];
			itens.push(item)
			
			//remove todos marcadores existentes no mapa:
			markers.map(function (item) { item.remove() });

			if (itens != null && itens.length > 0) {
				criarMarcadores(itens);
			}

		});
	}, (5 * 1000));
}

// Busca os dados das viagens ativas no sistema;
function getData(id) {
	return $.ajax({
		type: "get",
		url: "/api/equipamento/" + id,
		cache: false,
		Accept: "application/json",
		contentType: "application/json",
		success: function (response) {
			return response;
		},
		error: function (response, status, error) {
			console.log("Não foi possivel coletar dados no sistema. Entre em contato com o administrador do Sistema.");
		}
	});
}

// Função que cria e atualiza os marcadores:
function criarMarcadores(_viagens) {
	//Verifica se existem viagens:
	if (_viagens == null || _viagens.length == 0) return;

	$.each(_viagens, function (idx, viagem) {
		if (viagem.detalhes != null) {

			// Pega o ultimo detalhe (ultima localização):
			var ultimoDetalhe = viagem.detalhes[viagem.detalhes.length - 1];

			if (ultimoDetalhe != null) {
				//Cria o icone do marcador com a cor informada no cadastro:
				var _icon = L.AwesomeMarkers.icon({
					icon: 'cube',
					prefix: 'ion',
					markerColor: 'white',
					iconColor: '#153649',
					spin: false
				});

				// configura o marcador com o icone, tooltip:
				var options = {
					icon: _icon,
					tooltip: {
						html: "<b><i class='fa fa-thermometer-empty'></i> Temperatura Atual:</b> " + ultimoDetalhe.numTemperaturaDeta + "ºC."
					}
				};
				
				var marker = L.marker([ultimoDetalhe.numLatitudeDeta, ultimoDetalhe.numLongitudeDeta], options).addTo(map);
				markers.push(marker);
			}

		}
	});
}

// Monta um objeto com as coordenadas de acesso do usuário corrente:
function getPositionOptions() {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(function (position) {
			return { center: [position.coords.latitude, position.coords.longitude], zoom: 12 };
		});
	}
}

// Busca um marcador existente na mapa:
function getMarkerInMap(viagemId) {
	if (markers == null) return null;

	return markers.find(function (item) {
		return item.options.viagemId == viagemId;
	})
}
