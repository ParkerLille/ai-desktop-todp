export type EntityId = string;

export type WorkspaceId = EntityId;
export type TaskId = EntityId;
export type WindowId = EntityId;
export type WorkflowRunId = EntityId;

export type ResultEnvelope<T> = {
  data: T;
  traceId: string;
};

export type ErrorEnvelope = {
  code: string;
  message: string;
  details?: unknown;
  traceId?: string;
  retryable: boolean;
};
