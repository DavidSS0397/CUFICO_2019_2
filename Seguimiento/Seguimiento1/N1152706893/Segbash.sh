for i in {1..7}; do mkdir Folder${i};  cd Folder${i}; for j in {1..10}; do touch Archivo${j}; echo "Holiiii" > Archivo${j}; done; cd -; done
