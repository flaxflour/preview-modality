<template>
  <div class="full-screen">
    <div v-if="loading" class="content">Content is loading...</div>
    <div v-else>
      <FloatingWindow
        :loading="loading"
        :type-of-content="typeOfContent"
        :set-is-open="(value) => (isOpen = value)"
        :width="initialWidth"
        :height="initialHeight"
        :url="url"
        :type="type"
      />
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import FloatingWindow from "./components/FloatingWindow.vue";

defineProps({
  msg: String,
});

const count = ref(0);

const refresh = () => window.location.reload();

const isOpen = ref(false);
const loading = ref(true);
const typeOfContent = ref("image");
const initialWidth = null;
const initialHeight = null;
const type = ref("image/png");
const url = ref("");

const log = () => console.log("hii");

onMounted(async () => {
  window.me = loading;
  loading.value = false;
  type.value = "pdf";
  return;
  let item = "";
  await fetch("/api/v1/items/63a2d87ac0338c976b73a49d", {
    headers: {
      "Content-Type": "application/json;charset=UTF-8",
      "Access-Control-Allow-Origin": "*",
      Authorization:
        "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFqQTVPRVF3Umpnek9ESXdNa1E1UmpjMU5VVXpRMFJGTXpsRE9URTBOMEZGUVVZMk0wWkJPQSJ9.eyJodHRwczovL2RhdGFsb29wLmFpL2F1dGhvcml6YXRpb24iOnsiZ3JvdXBzIjpbXSwicm9sZXMiOltdLCJ1c2VyX3R5cGUiOiJodW1hbiJ9LCJnaXZlbl9uYW1lIjoiRGVsbCIsImZhbWlseV9uYW1lIjoiWFBTIiwibmlja25hbWUiOiJhbGlldl9hbWlyemhhbmkiLCJuYW1lIjoiRGVsbCBYUFMiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUVkRlRwN1RBS3cza0NrUVJpMVc4VTRYOFVXTkZhR0NXQVN4SVdNZVZ0UjA1Zz1zOTYtYyIsImxvY2FsZSI6InJ1IiwidXBkYXRlZF9hdCI6IjIwMjItMTItMjFUMDk6NTE6MjkuOTI3WiIsImVtYWlsIjoiYWxpZXZfYW1pcnpoYW5pQG1haWwucnUiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6Ly9kYXRhbG9vcC1wcm9kdWN0aW9uLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMDkyNzIwNjk1MzMyMDEwNTU3NiIsImF1ZCI6IkZyRzBIWmdhMUNLNVVWVVNKSnVEa1NEcUl0UGllV0dXIiwiaWF0IjoxNjcxNzAyNDEyLCJleHAiOjE2NzE3ODg4MTJ9.qp6VQZGJfeGvo0-9p1TeDwp1Iov2TWWEhb5bsO8hcWjsBPU7LP2yjBzIWzoSo6OrY1V7wLOeD_We1DGs-BKX9dF68o3W7GYLEaTGrny0UNl7_BQRS2xs5iX7oHPxlF6BrBAddZwcD_lnl-n34BcUXcIzhYwEvXswo6BEJP0sX4SrlByExNSIyr3KQ3RWPlsS2e9mGcd3N2ySohBjWX4CBw-fj5jGlPgbdeHGhWTXHyQjGM0nyBhEwCEMpMff32_qdzV9MJs1ruG2rmy02jvWLDEoz4tGRs7MHuv7cift71i7zgH4rNcgIH6hbfFEeJU1VK7JkbvkSFxsrWvKPDdyCg",
      // 'Cookie': 'sails.sid=s%3AvnaA_ExnI7uxwHAB3cIt_mFEtxyhoFmx.Az8BEnvBcHQ4GdMl6npILjBS%2F9Brh%2BEFi2vQsGunWVc; JWT=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFqQTVPRVF3Umpnek9ESXdNa1E1UmpjMU5VVXpRMFJGTXpsRE9URTBOMEZGUVVZMk0wWkJPQSJ9.eyJodHRwczovL2RhdGFsb29wLmFpL2F1dGhvcml6YXRpb24iOnsiZ3JvdXBzIjpbXSwicm9sZXMiOltdLCJ1c2VyX3R5cGUiOiJodW1hbiJ9LCJnaXZlbl9uYW1lIjoiRGVsbCIsImZhbWlseV9uYW1lIjoiWFBTIiwibmlja25hbWUiOiJhbGlldl9hbWlyemhhbmkiLCJuYW1lIjoiRGVsbCBYUFMiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUVkRlRwN1RBS3cza0NrUVJpMVc4VTRYOFVXTkZhR0NXQVN4SVdNZVZ0UjA1Zz1zOTYtYyIsImxvY2FsZSI6InJ1IiwidXBkYXRlZF9hdCI6IjIwMjItMTItMjFUMDk6NTE6MjcuMDkxWiIsImVtYWlsIjoiYWxpZXZfYW1pcnpoYW5pQG1haWwucnUiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6Ly9kYXRhbG9vcC1wcm9kdWN0aW9uLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMDkyNzIwNjk1MzMyMDEwNTU3NiIsImF1ZCI6IkZyRzBIWmdhMUNLNVVWVVNKSnVEa1NEcUl0UGllV0dXIiwiaWF0IjoxNjcxNjE2Mjg5LCJleHAiOjE2NzE3MDI2ODksImNfaGFzaCI6InFINzZsVHEyekpQZmpFal9COGh4MlEiLCJzaWQiOiI0QnNwb1hYWnAtdjVROHFUYVdaMmRiTy1heFk4VHpqOSIsIm5vbmNlIjoiMEg4U3hmQWE1bGswQ1NUNm5nYzdOYUFQWTAzbzdzd2wifQ.UgrcH8o2odjoB6cb9GUmMHjrDpDHh-dOMRiseg-HJLqDeMFKe9rrLmSLjc23zRMzKKB_qTTcAr2vb7xN8amJFno9OQ-lFa7p6QShgmKQCgpH9BlSaYLupAtb7alssEIH6oUVbuVTy40XLf5LdV-TjcQrehM8jnkqkwe39ATyVyiwDuxw6-sjFhIUIrZ3RCSE6fW0-kWW4xmCinNi4quMJ82CLELhljM2_aJm_MJsRLVO3imqfeFuBoBxgCVEfpqSm6tLppfX1bDCTfd7mCY6MVGXVfL5VVZ1J2ld4LFp0e4thL6UGhZ5_tls4ebOfO9UGqwyKKELlnKUgamY9MVLpQ; refresh_token=sl-HKDBRDF03n79F5sJKldl-wDaQpUoEm16_DnoImcv3v'
    },
  })
    .then((resp) => resp.json())
    .then((resp) => (item = resp));
  console.log(item);

  // await dl.init()
  // dl.on('ready', async () => {
  // const item = await dl.items.get()
  console.log(`item fetched -`, { item });
  const previewModality = item.metadata.system.modalities.find(
    (m) => m.type === "preview"
  );
  if (previewModality) {
    if (true || previewModality.refType === "url") {
      url.value = previewModality.ref;
      type.value = previewModality.mimetype;
    } else {
      const modalityItem = await dl.items.stream(previewModality.stream);
      url.value = modalityItem;
      // type.value = modalityItem.metadata?.system?.mimetype
      // const width = modalityItem.metadata.system.width
      // const height = modalityItem.metadata.system.height
      // await dl.app.updateSlotSettings({ width, height })
    }
    typeOfContent.value = type.value.split("/")[0];
  }
  loading.value = false;
  url.value = "https://cdn.filestackcontent.com/wcrjf9qPTCKXV3hMXDwK";

  // })
});
</script>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}

.content {
  width: 100%;
  height: 100%;
  display: grid;
  place-items: center;
}
</style>
