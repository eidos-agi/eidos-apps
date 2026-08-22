/**
 * eidos-apps SDK — opinions as types.
 * Do not grow this into Applets. Do not name it Prim App.
 */

/** Prim Tools are operators on a Prim. Do not mint prim.surface / prim.connector packs. */
export type PrimToolKind = "surface" | "connector";

export type PrimCite = {
  profile: string;
  path: string;
};

export type ToolCite = {
  kind: PrimToolKind;
  name: string;
  cites: PrimCite;
};

export type Surface = {
  id: string;
  title: string;
  /** A real page. Not a json-render card. */
  url: string;
};

/**
 * A human yes. The agent stops. Silence is not a pass.
 */
export type Gate = {
  id: string;
  title: string;
  pass: "human-yes";
};

export type StoreOpinion = {
  kind: "sqlite-vec" | "files";
  path: string;
};

/** Apps run as containers. Applets are local workers. Do not swap them. */
export type DockerRuntime = {
  kind: "docker";
  image: string;
};

export type AppApi = {
  call(method: string, args?: unknown): Promise<unknown>;
};

export type AppAdapters = {
  mcp?: boolean;
  cli?: boolean;
};

export type EidosApp = {
  kind: "eidos-app";
  id: string;
  name: string;
  summary: string;
  prims: PrimCite[];
  tools: ToolCite[];
  surfaces: Surface[];
  gates: Gate[];
  store: StoreOpinion;
  runtime: DockerRuntime;
  api: AppApi;
  adapters?: AppAdapters;
};

export type CliAdapter = {
  enabled: true;
  expose(api: AppApi): void;
};

export type McpAdapter = {
  enabled: true;
  expose(api: AppApi): void;
};

export function requireGates(app: EidosApp): Gate[] {
  if (!app.gates.length) {
    throw new Error("an Eidos App needs at least one human gate");
  }
  return app.gates;
}
