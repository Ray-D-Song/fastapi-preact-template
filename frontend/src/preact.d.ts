import { JSX } from "preact";

declare global {
  namespace JSX {
    interface IntrinsicElements extends JSX.IntrinsicElements {}
  }
}

declare module "react" {
  export = preact;
  export as namespace preact;
}

declare module "react-dom" {
  export * from "preact/compat";
}
