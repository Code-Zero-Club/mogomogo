import { mogoSelector } from "../components/mogoSelector";

export default function goPage() {
    return (
        <div className="text-center m-6">
            <h1 className="font-black text-2xl">모의고사 선택</h1>
            <mogoSelector>고2 2024년 11월</mogoSelector>
            <div className="mt-10 mx-auto font-semibold max-w-80 border border-slate-700 p-3 rounded-xl">고2 2024년 9월<br/>(준비중)</div>
        </div>
    );
}