<template>
    <div class="container">
        <h1 class="mt-5">{{ project.name }}</h1>
        <div>
            <img class="img-style" @click="openFullScreen" v-bind:src="project.get_image" >
        </div>
        <div class="mt-4">
            <div>
                <p class="text-start me-auto text-black"><strong>{{ project.description }}</strong></p>
            </div>
        </div>
        <div v-if="isFullScreen" class="fullscreen-image" @click="closeFullScreen">
            <img :src="project.get_image" class="fullscreen-img" />
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Project',
    data() {
        return {
            imageUrl: '',
            isFullScreen: false,
            project: {}
        }
    },
    methods: {
        openFullScreen() {
            this.isFullScreen = true;
            const element = document.documentElement;
            if (element.requestFullscreen) {
                element.requestFullscreen();
            } else if (element.mozRequestFullScreen) {
                element.mozRequestFullScreen();
            } else if (element.webkitRequestFullscreen) {
                element.webkitRequestFullscreen();
            } else if (element.msRequestFullscreen) {
                element.msRequestFullscreen();
            }
        },
        closeFullScreen() {
            this.isFullScreen = false;
            // Esci dalla modalità a schermo intero solo se è attiva
            if (document.fullscreenElement || document.mozFullScreenElement || document.webkitFullscreenElement || document.msFullscreenElement) {
                if (document.exitFullscreen) {
                    document.exitFullscreen();
                } else if (document.mozCancelFullScreen) {
                    document.mozCancelFullScreen();
                } else if (document.webkitExitFullscreen) {
                    document.webkitExitFullscreen();
                } else if (document.msExitFullscreen) {
                    document.msExitFullscreen();
                }
            }
        },
        getProjectDetail() {
            const project_slug = this.$route.params.project_slug
            axios.get(`/api/v1/projects/${project_slug}/`)
                .then(response => {
                    this.project = response.data
                    document.title = this.project.name
                }).catch(error => {
                    console.log(error)
                })
        }
    }, mounted() {
        this.getProjectDetail()
    }
}
</script>
<style scoped>
.fullscreen-image {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.8);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 9999;
    cursor: pointer;
}

.fullscreen-img {
    max-width: 90%;
    max-height: 90%;
}

/* Stile aggiuntivo per l'immagine principale quando non è a schermo intero */
.img-style {
    border: solid 1px;
    border-color: black;
    width: 50%;
    height: 100%;
}

/* Rimuovi il focus blu quando si fa clic su un'immagine */
.img-style:focus {
    outline: none;
}

.img-style {
    border: solid 1px;
    border-color: black;
    height: 400px;
}

.p-style {
    text-decoration-color: black;
}
</style>