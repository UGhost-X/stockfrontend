<template>
  <slot :name="logshow">
    {{ svgheight }}--{{ svgwidth }}
  </slot>
</template>

<script setup>
import { ref } from "vue";

const props = defineProps({
  width: {
    type: Number,
  },
  height: {
    type: Number,
  },
});

const svgwidth = ref(props.width);
const svgheight = ref(props.height);
</script>
