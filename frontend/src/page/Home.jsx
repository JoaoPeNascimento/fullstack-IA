import { useState } from "react";
import TextInput from "../components/TextInput";
import SummaryOutput from "../components/SummaryOutput";
import Loader from "../components/Loader";
import { summarizeText } from "../api/summarize";

export default function App() {
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async (text) => {
    setLoading(true);
    setResult("");

    try {
      const data = await summarizeText(text);
      setResult(data.result.summary_text || "Nenhum resultado retornado.");
    } catch (error) {
      setResult("Erro ao se conectar com o servidor." + error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <div className="min-h-screen min-w-screen flex flex-col items-center justify-center bg-gradient-to-br from-gray-900 via-indigo-900 to-black text-white px-4 py-8">
        <h1 className="text-3xl sm:text-4xl font-extrabold mb-6 text-indigo-400 tracking-tight">
          🧠 Analisador de Texto com IA
        </h1>

        <TextInput onAnalyze={handleAnalyze} />

        {loading && <Loader />}
        {!loading && <SummaryOutput result={result} />}
      </div>
    </>
  );
}
