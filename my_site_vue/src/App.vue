<template>
    <nav class="mt-5">
        <a href="/" class='router-link-active router-link-exact-active custom-link me-1' aria-current="page" to="/">
            <strong>Home</strong>
        </a>
        |
        <a href="/projects" class='router-link-active router-link-exact-active custom-link ms-1' aria-current="page" to="/">
            <strong>I miei progetti</strong>
        </a>
        
    </nav>
    <router-view />
</template>

<script>
import axios from 'axios';

export default {

}
</script>

<style>
.welcome-message {
    font-family:initial ;
}

.custom-link {
    color:  burlywood;
    text-decoration: none;
}

.padding {
    padding-top: 40px;
    padding-right: 30px;
    padding-bottom: 40px;
    padding-left: 80px;
}

.text_color {
    text-decoration-color: #704E2E;
}
</style>
