@media (max-width: 768px) {
    /* 1. Resetear contenedores con márgenes excesivos */
    .hero, .clients, .community, .unlock, .achievements, 
    .calender, .customer, .update, .dot, .copy, .links, .email {
        padding-left: 20px !important;
        padding-right: 20px !important;
        padding-top: 50px;
        padding-bottom: 50px;
    }

    /* 2. Convertir Grids y Flexbox a una sola columna */
    header {
        flex-direction: column;
        align-items: center;
        text-align: center;
    }

    .nav, .login, .main, .clients-logos, .images-comunity, 
    .unlock, .counts, .calender, .customer, .main-footer, .links {
        display: flex;
        flex-direction: column;
        margin-left: 0 !important;
        margin-top: 20px !important;
        align-items: center;
        text-align: center;
    }

    /* 3. Ajustar textos grandes */
    .text h2, .dot h1 {
        font-size: 35px;
    }

    .secondary h2 {
        margin-top: 0;
    }

    /* 4. Ajustar imágenes para que no se desborden */
    .images-main, .unlock img, .calender img, .customer .img-tesla {
        margin-left: 0;
        height: auto;
        max-width: 100%;
    }

    /* 5. Navegación y Botones */
    .nav a {
        padding: 10px;
        display: block;
    }

    .butons-comunity {
        position: static;
        padding-left: 0;
    }

    /* 6. Footer */
    .redes {
        grid-template-columns: repeat(4, 1fr);
        justify-content: center;
    }

    .redes i {
        margin: 20px 10px;
    }

    .input {
        width: 100%;
        max-width: 300px;
    }
}
