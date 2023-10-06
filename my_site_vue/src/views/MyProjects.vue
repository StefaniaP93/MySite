<template>
    <div class="container mt-5">
        <h1 class="mb-5 text-light">I miei progetti:</h1>
        <div class="row">
            <div v-for="project in projects" :key="project.id">
                <figure class="figure">
                    <img :src="project.get_image" class="carousel-image card-img" alt="...">
                    <router-link :to="{ name: 'Project', params: { project_slug: project.get_absolute_url } }"
                        class="figure-caption text-light">
                        {{ project.name }}
                    </router-link>
                </figure>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios';

export default {
    name: 'MyProjects',
    data() {
        return {
            projects: []
        }
    },
    mounted() {
        this.getProjects()
        document.title = 'My Projects | '
    },
    methods: {
        getProjects() {
            axios.get('/api/v1/projects/')
                .then(response => {
                    this.projects = response.data
                }).catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>

<style scoped>
.carousel-image {
    max-width: 100%;
    /* Imposta la larghezza massima al 100% per adattare automaticamente le dimensioni */
    max-height: 300px;
    /* Imposta l'altezza massima desiderata */
    margin: 0 auto;
    /* Centra l'immagine orizzontalmente */
}
</style>