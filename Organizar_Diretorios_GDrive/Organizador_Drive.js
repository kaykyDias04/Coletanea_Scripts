function executarOrganizadorComPausa() {
  var props = PropertiesService.getScriptProperties();
  var idPastaParaProcessar = props.getProperty('PROXIMA_PASTA_ID');
  
  var pastaInicial = idPastaParaProcessar ? 
      DriveApp.getFolderById(idPastaParaProcessar) : 
      DriveApp.getRootFolder();
  
  Logger.log("Iniciando/Retomando organização na pasta: " + pastaInicial.getName());
  
  var tempoInicio = new Date().getTime();
  var interrompido = organizarPorCriacaoComLimite(pastaInicial, tempoInicio);

  if (interrompido) {
    Logger.log("Tempo limite quase atingido. Criando agendamento para continuar...");
    criarGatilhoDeRetomada();
  } else {
    Logger.log("Organização completa! Removendo checkpoints.");
    props.deleteProperty('PROXIMA_PASTA_ID');
    removerGatilhos();
  }
}

function organizarPorCriacaoComLimite(pastaAtual, tempoInicio) {
  var props = PropertiesService.getScriptProperties();
  var meses_pt = {
    0: "01 - Janeiro", 1: "02 - Fevereiro", 2: "03 - Março",
    3: "04 - Abril", 4: "05 - Maio", 5: "06 - Junho",
    6: "07 - Julho", 7: "08 - Agosto", 8: "09 - Setembro",
    9: "10 - Outubro", 10: "11 - Novembro", 11: "12 - Dezembro"
  };

  var tempoAtual = new Date().getTime();
  if (tempoAtual - tempoInicio > 300000) { // 300.000 ms = 5 min
    props.setProperty('PROXIMA_PASTA_ID', pastaAtual.getId());
    return true;
  }

  var valoresMeses = Object.values(meses_pt);
  if (valoresMeses.indexOf(pastaAtual.getName()) !== -1 || pastaAtual.getName().match(/^\d{4}$/)) {
    return false;
  }

  var arquivos = pastaAtual.getFiles();
  while (arquivos.hasNext()) {
    var arquivo = arquivos.next();
    var dataCriacao = arquivo.getDateCreated();
    var ano = dataCriacao.getFullYear().toString();
    var mesNome = meses_pt[dataCriacao.getMonth()];

    var pastaAno = obterOuCriarPasta(pastaAtual, ano);
    var destinoPasta = obterOuCriarPasta(pastaAno, mesNome);

    try {
      arquivo.moveTo(destinoPasta);
    } catch (e) {
      Logger.log("Erro ao mover " + arquivo.getName() + ": " + e.toString());
    }
  }

  var subpastas = pastaAtual.getFolders();
  while (subpastas.hasNext()) {
    var subpasta = subpastas.next();
    var interrompeuNaSub = organizarPorCriacaoComLimite(subpasta, tempoInicio);
    if (interrompeuNaSub) return true;
  }

  return false;
}

function obterOuCriarPasta(pastaPai, nomePasta) {
  var pastas = pastaPai.getFoldersByName(nomePasta);
  return pastas.hasNext() ? pastas.next() : pastaPai.createFolder(nomePasta);
}

function criarGatilhoDeRetomada() {
  removerGatilhos();
  ScriptApp.newTrigger('executarOrganizadorComPausa')
           .timeBased()
           .after(60000)
           .create();
}

function removerGatilhos() {
  var gatilhos = ScriptApp.getProjectTriggers();
  for (var i = 0; i < gatilhos.length; i++) {
    ScriptApp.deleteTrigger(gatilhos[i]);
  }
}
