<template>
  <div class="audio-recorder">
    <h2>Grabador de Audio</h2>
    <button @click="startRecording" :disabled="isRecording">Iniciar Grabación</button>
    <button @click="stopRecording" :disabled="!isRecording">Detener Grabación</button>
    <audio v-if="audioUrl" :src="audioUrl" controls></audio>
    <button v-if="audioUrl" @click="uploadAudio">Subir Audio</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isRecording: false,
      mediaRecorder: null,
      audioChunks: [],
      audioUrl: null,
    };
  },
  methods: {
    async startRecording() {
      this.audioChunks = [];
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      this.mediaRecorder = new MediaRecorder(stream);
      this.mediaRecorder.start();
      this.isRecording = true;

      this.mediaRecorder.ondataavailable = (event) => {
        this.audioChunks.push(event.data);
      };

      this.mediaRecorder.onstop = () => {
        const audioBlob = new Blob(this.audioChunks, { type: 'audio/wav' });
        this.audioUrl = URL.createObjectURL(audioBlob);
      };
    },
    stopRecording() {
      this.mediaRecorder.stop();
      this.isRecording = false;
    },
    uploadAudio() {
      const formData = new FormData();
      formData.append('audio', this.audioChunks[0], 'recording.wav');

      fetch('/api/upload', {
        method: 'POST',
        body: formData,
      })
      .then(response => response.json())
      .then(data => {
        console.log('Audio uploaded successfully:', data);
      })
      .catch(error => {
        console.error('Error uploading audio:', error);
      });
    },
  },
};
</script>

<style scoped>
.audio-recorder {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>