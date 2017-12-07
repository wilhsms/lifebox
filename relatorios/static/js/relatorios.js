
  //Ajax responsável por trazer os dados da viagem no modal
  function openModal(id) {
    $.ajax({
      type: "get",
      url: "/api/viagem/" + id,
      cache: false,
      Accept: "application/json",
      contentType: "application/json",
      success: function (viagem) {
        var detalhesHtml = '';        
        $.each(viagem.detalhes, function (idx, detalhe) {
          detalhesHtml = detalhesHtml + 
            '<tr>'+
                '<td>'+moment(detalhe.datDataHoraDeta).format('DD/MM/YYYY HH:MM:ss')+'</td>'+
                '<td class="center">'+(detalhe.indVirouDeta ? 'Sim' : 'Não')+'</td>'+
                '<td class="center">'+(detalhe.indTombouDeta ? 'Sim' : 'Não')+'</td>'+
                '<td class="center">'+detalhe.numTemperatura1Deta+'º</td>'+
                '<td class="center">'+detalhe.numTemperatura2Deta+'º</td>'+
                '<td>'+detalhe.numElevacaoDeta+' pés</td>'+
                '<td>'+detalhe.numVelocidadeDeta+'km/h</td>'+
            '</tr>'
				});
        
        $('#modal_relatorio').html(
          //Cabeçalho com dados ficticios a serem preenchidos pela API
          '<h5 class="texto_detalhes_modal">INFORMAÇÕES SOBRE O EQUIPAMENTO</h5>'+
          '<div class="row">'+
              '<div class="col-sm-3">'+
                '<p class="texto_detalhe_modal">Caixa:</p>'+
                '<label>'+
                  '<span style="color : '+viagem.caixa.corCaixa+'">'+
                    '<i class="ion-cube"></i>'+
                  '</span> '+ viagem.caixa.idCaixa +
                '</label>'+
              '</div>'+
              '<div class="col-sm-3">'+
                '<p class="texto_detalhe_modal">Nº Autorização:</p>'+
                '<label>'+ viagem.caixa.autorizacao+'</label>'+
              '</div>'+
          '</div>'+
          '<div class="row">'+
              '<div class="col-sm-3">'+
                '<p class="texto_detalhe_modal">Equipamento:</p>'+
                '<label>'+ viagem.equipamento.idEquipamento+'</label>'+
              '</div>'+
              '<div class="col-sm-3">'+
                '<p class="texto_detalhe_modal">IMEI:</p>'+
                '<label>'+ viagem.equipamento.imeiEquipamento+'</label>'+
              '</div>'+
          '</div>'+
          '<h5 class="texto_detalhes_modal">INFORMAÇÕES SOBRE O TRAJETO</h5>'+
            '<div class="row">'+
              '<div class="col-sm-6">'+
                '<p class="texto_detalhe_modal">Local de Partida:</p>'+
                '<label>'+viagem.localPartida.nome+'</label>'+
              '</div>'+
              '<div class="col-sm-6">'+
                '<p class="texto_detalhe_modal">Responsável:</p>'+
                '<label>'+ viagem.localPartida.nomeResponsavel+'</label>'+
              '</div>'+
            '</div>'+
            '<div class="row">'+
              '<div class="col-sm-6">'+
                '<p class="texto_detalhe_modal">Local de Chegada:</p>'+
                '<label>'+ viagem.localChegada.nome+'</label>'+
              '</div>'+
              '<div class="col-sm-6">'+
                '<p class="texto_detalhe_modal">Responsável:</p>'+
                '<label>'+ viagem.localChegada.nomeResponsavel+'</label>'+
              '</div>'+
            '</div>'+
            '<hr>'+
            '<div class="row">'+
              '<div class="col-sm-6">'+
                '<p class="texto_detalhe_modal">Transportador:</p>'+
                '<label>'+ viagem.nomeTransportador+'</label>'+
              '</div>'+
              '<div class="col-sm-3">'+
                '<p class="texto_detalhe_modal">Início da Viagem:</p>'+
                '<label>'+ moment(viagem.dataInicio).format('DD/MM/YYYY HH:MM:ss')+'</label>'+
              '</div>'+
              '<div class="col-sm-3">'+
                '<p class="texto_detalhe_modal">Fim da Viagem:</p>'+
                '<label>'+ moment(viagem.dataFim).format('DD/MM/YYYY HH:MM:ss')+'</label>'+
              '</div>'+
            '</div>'+
          '<h5 class="texto_detalhes_modal">DETALHAMENTO DA VIAGEM</h5>'+
          '<div class="row">'+
            '<div class="col-sm-12">'+
               '<table class="table table-striped">'+
                  '<thead>'+
                      '<tr>'+
                          '<th>Data/Hora</th>'+
                          '<th>Tombo?</th>'+
                          '<th>Virou?</th>'+
                          '<th>Temp. Interna</th>'+
                          '<th>Temp. Externa</th>'+
                          '<th>Elevação</th>'+
                          '<th>Velocidade</th>'+
                      '</tr>'+
                  '</thead>'+
                  '<tbody>'+
                    detalhesHtml +
                  '</tbody>'+
                '</table>' + 
              '</div>'+
            '</div>'
        );

        //$('#exampleModalLong').modal('show');
      },
      error: function (response, status, error) {
        console.log(
          "Não foi possivel coletar as viagens no sistema. Entre em contato com o administrador do Sistema."
        );
      }
    });
  }

  //Configuração do datatable
  $(document).ready(function () {
    $('#busca').DataTable({
      "searching": false,
      "scrollY": 210, //ativa rolagem vertical - valor define o altura da tabela em px
      "scrollX": true, // ativa barra de rolagem horizontal, quando necessário
      "scrollCollapse": true, // não sei, ainda
      "paging": true, // ativa pagnação da tabela
      "ordering": false,
      "aLengthMenu": [
        [05, 10, 25, 50, 75, 100, -1],
        [05, 10, 25, 50, 75, 100, "All"]
      ], // opções para quantidade de linhas exibidas
      "iDisplayLength": 10, // padrão para inicio da tabela esta função não funciona com stateSave =true

      stateSave: true, // permite salvar a ultima pesquisa realizada.

      "language": {
        "decimal": ",",
        "thousands": ".",
        "sEmptyTable": "Nenhum registro encontrado",
        "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
        "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
        "sInfoFiltered": "(Filtrados de _MAX_ registros)",
        "sInfoPostFix": "",
        "sInfoThousands": ".",
        "sLengthMenu": "_MENU_ resultados por página",
        "sLoadingRecords": "Carregando...",
        "sProcessing": "Processando...",
        "sZeroRecords": "Nenhum registro encontrado",
        "sSearch": "Pesquisar",
        "oPaginate": {
          "sNext": "Próximo",
          "sPrevious": "Anterior",
          "sFirst": "Primeiro",
          "sLast": "Último"
        },
        "oAria": {
          "sSortAscending": ": Ordenar colunas de forma ascendente",
          "sSortDescending": ": Ordenar colunas de forma descendente"
        }
      }
    });

    //JS responsável pela impressão.
    $("#btnImprimir").on("click", function () {
      var content = $('.modal-body').html();
      var printWindow = window.open('', '', 'height=400,width=800');
      printWindow.document.write(
        '<html><head><title>Relatório da Viagem</title>' +
        bootstrap +
        relatorio_estilos);
      printWindow.document.write('</head><body>');
      printWindow.document.write(content);
      printWindow.document.write('</body></html>');
      printWindow.document.close();
      printWindow.print();
    });

  });

  //foi
