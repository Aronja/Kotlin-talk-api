echo kotlin will be compiled
kotlinc kotlin.kt -include-runtime -d kotlin.jar
echo kotlin is compiled
java -jar kotlin.jar
echo done!