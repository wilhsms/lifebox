
  //Ajax responsável por trazer os dados da viagem no modal
  function openModal(id) {
    $.ajax({
      type: "get",
      url: "/api/viagem/ativas/" + id,
      cache: false,
      Accept: "application/json",
      contentType: "application/json",
      success: function (viagem) {
        $('.modal-body').html(
          "Local de partida: <label> " + viagem.localPartida.nome + "</label><br/>" +
          "Local de chegada: <label> " + viagem.localChegada.nome + "</label><br/>" +
          "Caixa: <label> " + viagem.caixa.idCaixa + "</label><br/>" +
          "Equipamento: <label> " + viagem.equipamento.idEquipamento + "</label>"
        )

        $('#modal_relatorio').modal('show');
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
      var content = $('#modal_relatorio').html();
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

  