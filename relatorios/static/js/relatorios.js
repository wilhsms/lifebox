
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
                '<td>'+(detalhe.indVirouDeta ? 'Sim' : 'Não')+'</td>'+
                '<td>'+(detalhe.indTombouDeta ? 'Sim' : 'Não')+'</td>'+
                '<td>'+detalhe.numTemperatura1Deta+' º</td>'+
                '<td>'+detalhe.numTemperatura2Deta+' º</td>'+
                '<td>'+detalhe.numElevacaoDeta+' pés</td>'+
                '<td>'+detalhe.numVelocidadeDeta+' km/h</td>'+
            '</tr>'
				});
        
        $('#modal_relatorio').html(
          //Cabeçalho com dados ficticios a serem preenchidos pela API
          '<h5 class="texto_detalhes_modal">INFORMAÇÕES SOBRE O EQUIPAMENTO</h5>'+
          '<div class="col-xl-12">'+
              '<p class="texto_detalhe_modal">Caixa:</p>'+
              '<label>'+viagem.caixa.idCaixa+'</label>'+
              '<p class="texto_detalhe_modal">LifeBox:</p>'+
              '<label>'+ viagem.equipamento.idEquipamento+'</label>'+
          '</div>'+
          '<h5 class="texto_detalhes_modal">INFORMAÇÕES SOBRE O TRAJETO</h5>'+
            '<div class="col-xl-12">'+
              '<p class="texto_detalhe_modal">Local de partida:</p>'+
              '<label>'+viagem.localPartida.nome+'</label>'+
              '<p class="texto_detalhe_modal">Local de chegada:</p>'+
            
              '<label>'+ viagem.localChegada.nome+'</label>'+
            '</div>'+
          '<h5 class="texto_detalhes_modal">DETALHAMENTO DA VIAGEM</h5>'+
          '<div class="col-xl-12">'+
             '<table border="0" class="table table-striped">'+
                '<thead>'+
                    '<tr>'+
                        '<th>Data/Hora</th>'+
                        '<th>Tombo?</th>'+
                        '<th>Virou?</th>'+
                        '<th>Temperatura Interna</th>'+
                        '<th>Temperatura Externa</th>'+
                        '<th>Elevação</th>'+
                        '<th>Velocidade</th>'+
                    '</tr>'+
                '</thead>'+
                '<tbody>'+
                  detalhesHtml +
                '</tbody>'+
              '</table>' + 
            '</div>'          
        );

        //$('#exampleModalLong').modal('show');
      },
      error: function (response, status, error) {
        console.log(
          "Não foi possivel coletar as viagens ativas no sistema. Entre em contato com o administrador do Sistema."
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
        '<html><head><title>Relatório da viagem</title>' +
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
