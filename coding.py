import os #sistema operativo
import random #numeri casuali


def cancellaRighe(directory, extensions=None, perc_lines=5, perc_chars=5):

    #se la directory NON è valida
    if not os.path.isdir(directory):
        raise ValueError("La directory passata non esiste.")
    
    #se extensions è none imposta lista è vuota
    if extensions is None:
        extensions = [""]
    
    #Iteriamo su tutti i file
    for root, _, files in os.walk(directory):
        for file in files:

            #se l'esstensione di ciascun file corrisponde a una delle estensioni passate come parametro.
            if any(file.endswith(estensione) for estensione in extensions):
                
                filepath = os.path.join(root, file) 
                with open(filepath, 'r') as modeR:           
                    lines = modeR.readlines()
                
                #itera ogni riga del file
                new_lines = []
                for line in lines:

                    #controlla se una riga deve essere cancellata in base alla percentuale perc_lines 
                    if random.random() > perc_lines/100:
                        new_lines.append(line)

                        #apri file modalità scrittura e scrivi nella lista newLines
                        with open(filepath, 'w') as modeW:
                            for line in new_lines:
                                modeW.write(line)

                        #apri file e leggi
                        with open(filepath, 'r') as modeR:
                            text = modeR.read()
                        
                        #itera ogni carattere
                        new_text = ""
                        for char in text:

                            #controlla se il carattere deve essere sostituito in base alla percentuale perc_chars
                            if random.random() > perc_chars/100:
                                new_text += char
                            else:
                                new_text += chr(random.randint(33, 126))
                        
                                with open(filepath, 'w') as f:
                                    f.write(new_text)
