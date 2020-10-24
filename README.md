# Hacking-Utils

Gestor de paquetes hkpac del proyecto Hacking-Utils.

### Sobre el proyecto

El proyecto Hacking-Utils tiene como finalidad principal proveer de software a los sistemas operativos más minimalistas, por ejemplo, Arch, Slackware, K1ss o Gentoo.

Hacking-Utils consiste en dos repositorios; el repositorio Hacking-Utils, que contiene el **gestor de paquetes hkpac**, y el repositorio hkprogs, que contiene todo el contenido que puede ser descargado e instalado fácilmente usando el **gestor de paquetes hkpac**.

### Sobre el repositorio

Este repositorio contiene el **gestor de paquetes hkpac** mediante el cual se puede descargar y administrar el contenido presente en el repositorio hkprogs del proyecto Hacking-Utils.

### Comandos

Para instalar paquetes se utiza la operación install. Para esto se debe contar con permisos elevados, Si el usuario no es el usuario root deberá ejecutar hkpac en conjunto con sudo o doas.

    sudo hkpac install [paquete]

Para actualizar el archivo de datos del repositorio, usa la operación update. Para esto se debe contar con permisos elevados, Si el usuario no es el usuario root deberá ejecutar hkpac en conjunto con sudo o doas.

    sudo hkpac update

Remover un archivo es sencillo y puede realizarse con la operación remove.

    hkpac remove [paquete]

Se puede utilizar la operación search en busca de paquetes.

    hkpac search [paquete]

La configuración puede manipularse con la operación config. Tras haber modificado un valor por primera vez, se creará un archivo de configuración, este se encuentra típicamente en /etc. Para realizar cambios en los ajustes se requiere de permisos elevados, excepto que se use la opción show, la operación config debe ejecutarse en conjunto con sudo o doas.

    sudo hkpac config [ajuste] [valor]
    sudo hkpac config [ajuste] default
    hkpac config [ajuste] show

### Escrito en

Hkpac fue escrito en Python.