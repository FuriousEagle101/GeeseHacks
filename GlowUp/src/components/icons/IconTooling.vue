<template>
  <div :style="{ fontSize: size }">
    🔒
  </div>
</template>

<script>
export default {
  props: {
    size: { type: String, default: "30px" }, // Default size is 64px
  },
};
</script>
