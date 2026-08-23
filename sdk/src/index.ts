/**
 * Eidos Apps contract — opinions as types.
 * The App is a Docker image. Do not grow this into Applets. Do not name it Prim App.
 */

/**
 * A connector cites a Prim. Not Prim’s `surface | connector` union.
 * App pages are Surface URLs, not Prim Tools.
 */
export type ConnectorKind = "connector";

export type PrimCite = {
  profile: string;
  path: string;
};

export type ToolCite = {
  kind: ConnectorKind;
  name: string;
  cites: PrimCite;
};

export type Surface = {
  id: string;
  title: string;
  /** App page. Not a Prim Tool. Not a json-render card. */
  url: string;
};

/**
 * Policy: a human yes is required.
 * This is not a record that anyone said yes.
 */
export type Gate = {
  id: string;
  title: string;
  requires: "human-yes";
};

export type StoreOpinion = {
  kind: "sqlite-vec" | "files";
  path: string;
};

/** The App is this image. dockerfile is the recipe in the pack. */
export type DockerRuntime = {
  kind: "docker";
  image: string;
  dockerfile: string;
};

/** Serializable pack. Matches app.json. No executable fields. */
export type AppManifest = {
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
};

export type AppApi = {
  call(method: string, args?: unknown): Promise<unknown>;
};

export type AppAdapters = {
  mcp?: boolean;
  cli?: boolean;
};

/** Runtime object once an image exists. Not in app.json. */
export type EidosApp = AppManifest & {
  api: AppApi;
  adapters?: AppAdapters;
};

export function requireGates(app: AppManifest): Gate[] {
  if (!app.gates.length) {
    throw new Error("an Eidos App needs at least one human gate");
  }
  return app.gates;
}
