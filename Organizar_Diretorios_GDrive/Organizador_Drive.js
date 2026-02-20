function executarOrganizadorNaRaiz() {
  var pastaRaiz = DriveApp.getRootFolder();
  
  Logger.log("Iniciando organização na raiz do Drive...");
  organizarPorCriacao(pastaRaiz);
  Logger.log("Organização concluída!");
}

function organizarPorCriacao(pastaAtual) {
  var meses_pt = {
    0: "Janeiro", 1: "Fevereiro", 2: "Marco",
    3: "Abril", 4: "Maio", 5: "Junho",
    6: "Julho", 7: "Agosto", 8: "Setembro",
    9: "Outubro", 10: "Novembro", 11: "Dezembro"
  };
  
  var valoresMeses = Object.values(meses_pt);
  
  if (valoresMeses.indexOf(pastaAtual.getName()) !== -1) {
    return; 
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
      
      var dataFormatada = Utilities.formatDate(dataCriacao, Session.getScriptTimeZone(), "dd/MM/yyyy");
      Logger.log("Criado em " + dataFormatada + " -> Movido para " + ano + "/" + mesNome);
    } catch (e) {
      Logger.log("Erro ao mover " + arquivo.getName() + ": " + e.toString());
    }
  }

  var subpastas = pastaAtual.getFolders();
  while (subpastas.hasNext()) {
    var subpasta = subpastas.next();
    
    organizarPorCriacao(subpasta);
  }
}

function obterOuCriarPasta(pastaPai, nomePasta) {
  var pastas = pastaPai.getFoldersByName(nomePasta);
  if (pastas.hasNext()) {
    return pastas.next();
  } else {
    return pastaPai.createFolder(nomePasta);
  }
}