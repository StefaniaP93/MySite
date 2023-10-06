<template>
    <div v-if="images && images.length">
        <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
            <div class="carousel-indicators">
                <button v-for="(image, index) in images" :key="index" type="button"
                    :data-bs-target="'#carouselExampleIndicators'" :data-bs-slide-to="index"
                    :class="{ active: index === 0 }" aria-label="Slide"></button>
            </div>
            <div class="carousel-inner">
                <div v-for="(project, index) in images" :key="index"
                    :class="{ 'carousel-item': true, active: index === 0 }">

                    <div class="d-flex justify-content-center align-items-center">
                        <img :src="project" class="carousel-image d-block w-80" alt="...">
                    </div>
                </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators"
                data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators"
                data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
            </button>
        </div>
    </div>
</template>
  
<script>
export default {
    name: 'Carousel',
    props: {
        images: Array,
    },
};
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
