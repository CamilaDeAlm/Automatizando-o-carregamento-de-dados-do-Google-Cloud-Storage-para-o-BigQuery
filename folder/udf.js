function transform(line) {
    var values = line.split(',');
    var obj = new Object();
    obj.id = values[0];
    obj.nome = values[1];
    obj.email = values[2];
    obj.idade = values[3];
    var jsonString = JSON.stringify(obj);
    return jsonString;
   }