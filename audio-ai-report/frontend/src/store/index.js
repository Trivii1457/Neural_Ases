import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    audioFile: null,
    report: null,
    loading: false,
    error: null,
  },
  mutations: {
    setAudioFile(state, audioFile) {
      state.audioFile = audioFile;
    },
    setReport(state, report) {
      state.report = report;
    },
    setLoading(state, loading) {
      state.loading = loading;
    },
    setError(state, error) {
      state.error = error;
    },
  },
  actions: {
    async uploadAudio({ commit }, audioFile) {
      commit('setLoading', true);
      commit('setError', null);
      commit('setAudioFile', audioFile);

      try {
        // Logic to upload audio and generate report
        // Example: const response = await api.uploadAudio(audioFile);
        // commit('setReport', response.data);
      } catch (error) {
        commit('setError', error.message);
      } finally {
        commit('setLoading', false);
      }
    },
  },
  getters: {
    audioFile: (state) => state.audioFile,
    report: (state) => state.report,
    loading: (state) => state.loading,
    error: (state) => state.error,
  },
});