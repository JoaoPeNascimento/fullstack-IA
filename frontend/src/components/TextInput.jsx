import { useState } from "react";

export default function TextInput({ onAnalyze }) {
  const [text, setText] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (text.trim()) {
      onAnalyze(text);
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="w-full bg-red max-w-2xl bg-white/10 backdrop-blur-md p-6 rounded-2xl shadow-lg border border-white/20"
    >
      <label className="block text-gray-100 font-semibold mb-2 text-lg">
        Digite o texto para análise:
      </label>
      <textarea
        className="w-full h-40 p-4 rounded-xl bg-gray-900/80 text-gray-100 border border-gray-700 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500 outline-none resize-none transition-all duration-200"
        placeholder="Cole aqui seu texto..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button
        type="submit"
        className="mt-4 w-full bg-indigo-600 hover:bg-indigo-700 text-white font-medium py-2.5 rounded-xl transition-all duration-200"
      >
        Analisar Texto
      </button>
    </form>
  );
}
