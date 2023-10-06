<template>
    <div>
        <div class="hello">
            <div class="padding"></div>
            <div class="container">
                <h1 class="welcome-message">Messaggio benvenuto</h1>
                <p class="text-center mt-5">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Sint, aut. Provident
                    reprehenderit eum architecto, accusamus saepe quibusdam aliquam ipsum iste voluptatem deleniti alias
                    voluptatum non, ducimus omnis earum, aspernatur illum.</p>
            </div>
            <hr>
        </div>
        <div class="container mt-4">
            <div class="row mt-5">
                <div class="col-6">
                    <Carousel :images="imageUrls" />
                </div>
                <div class="col-6 background_color">
                    <p class="text-start">
                        <strong>
                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Debitis laudantium, temporibus labore
                            officiis
                            praesentium ex doloremque perspiciatis maiores in facilis quaerat expedita unde at. Earum
                            commodi
                            doloribus
                            nesciunt dolore sit!
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad eum hic eaque minus quaerat odit
                            quia
                            mollitia. Distinctio vel nulla laudantium vero laborum ab, neque asperiores optio, autem, odio
                            exercitationem.
                        </strong>
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>
  

<script>
import axios from 'axios';
import Carousel from '@/components/Carousel.vue';

export default {
    name: 'HomeView',
    components: {
        Carousel,
    },
    data() {
        return {
            projects: [],
        };
    },
    computed: {
        imageUrls() {
            return this.projects.map((project) => project.get_image);
        },
    },
    mounted() {
        this.getCarouselImage();
    },
    methods: {
        getCarouselImage() {
            axios
                .get('/api/v1/projects-carousel/')
                .then((response) => {
                    this.projects = response.data;
                    console.log(response.data)
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    },
};
</script>

<style scoped>
.header_text {
    font-weight: 500;
    text-decoration-color: #FFE8D6;
    text-align: center;
    margin-top: 5%;
}
</style>