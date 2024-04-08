from . import extras
from .client import Client
from .lemur import Lemur
from .transcriber import RealtimeTranscriber, Transcriber, Transcript, TranscriptGroup
from .types import (
    AssemblyAIError,
    AudioEncoding,
    AutohighlightResponse,
    AutohighlightResult,
    Chapter,
    ContentSafetyLabel,
    ContentSafetyLabelResult,
    ContentSafetyResponse,
    ContentSafetySeverityScore,
    Entity,
    EntityType,
    IABLabelResult,
    IABResponse,
    IABResult,
    LanguageCode,
    LemurActionItemsResponse,
    LemurError,
    LemurModel,
    LemurPurgeRequest,
    LemurPurgeResponse,
    LemurQuestion,
    LemurQuestionAnswer,
    LemurQuestionResponse,
    LemurSource,
    LemurSourceType,
    LemurSummaryResponse,
    LemurTaskResponse,
    LemurTranscriptSource,
    Paragraph,
    PIIRedactionPolicy,
    PIISubstitutionPolicy,
    RawTranscriptionConfig,
    RealtimeError,
    RealtimeFinalTranscript,
    RealtimePartialTranscript,
    RealtimeSessionInformation,
    RealtimeSessionOpened,
    RealtimeTranscript,
    RealtimeWord,
    Sentence,
    Sentiment,
    SentimentType,
    Settings,
    SpeechModel,
    StatusResult,
    SummarizationModel,
    SummarizationType,
    Timestamp,
    TranscriptError,
    TranscriptionConfig,
    TranscriptStatus,
    Utterance,
    UtteranceWord,
    Word,
    WordBoost,
    WordSearchMatch,
)

settings = Settings()
"""Global settings object that applies to all classes that use the `Client` class."""


__all__ = [
    # types
    "AssemblyAIError",
    "AudioEncoding",
    "AutohighlightResponse",
    "AutohighlightResult",
    "Chapter",
    "Client",
    "ContentSafetyLabel",
    "ContentSafetyLabelResult",
    "ContentSafetyResponse",
    "ContentSafetySeverityScore",
    "Entity",
    "EntityType",
    "IABLabelResult",
    "IABResponse",
    "IABResult",
    "LanguageCode",
    "Lemur",
    "LemurActionItemsResponse",
    "LemurError",
    "LemurModel",
    "LemurPurgeRequest",
    "LemurPurgeResponse",
    "LemurSource",
    "LemurSourceType",
    "LemurTranscriptSource",
    "LemurQuestion",
    "LemurQuestionAnswer",
    "LemurQuestionResponse",
    "LemurSummaryResponse",
    "LemurTaskResponse",
    "PIIRedactionPolicy",
    "PIISubstitutionPolicy",
    "Sentence",
    "Sentiment",
    "SentimentType",
    "Settings",
    "SpeechModel",
    "StatusResult",
    "SummarizationModel",
    "SummarizationType",
    "Timestamp",
    "Transcriber",
    "TranscriptionConfig",
    "Transcript",
    "TranscriptError",
    "TranscriptGroup",
    "TranscriptStatus",
    "Utterance",
    "UtteranceWord",
    "Paragraph",
    "PIISubstitutionPolicy",
    "PIIRedactionPolicy",
    "RawTranscriptionConfig",
    "Word",
    "WordBoost",
    "WordSearchMatch",
    "RealtimeTranscriber",
    "RealtimeError",
    "RealtimeFinalTranscript",
    "RealtimePartialTranscript",
    "RealtimeSessionInformation",
    "RealtimeSessionOpened",
    "RealtimeTranscript",
    "RealtimeWord",
    # package globals
    "settings",
    # packages
    "extras",
]
