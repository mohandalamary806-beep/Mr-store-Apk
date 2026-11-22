/* MR Store — block long-press text selection, the copy/paste menu and image/link context menus.
   Form fields (input / textarea / contenteditable) and anything with class "allow-select" are exempt. */
(function () {
  'use strict';
  var EXEMPT = 'input, textarea, select, [contenteditable=""], [contenteditable="true"], .allow-select';

  function isExempt(node) {
    if (!node) return false;
    var el = node.nodeType === 1 ? node : node.parentElement;   // selectstart can target a text node
    return !!(el && el.closest && el.closest(EXEMPT));
  }
  function block(e) {
    if (!isExempt(e.target)) e.preventDefault();
  }

  document.addEventListener('contextmenu', block, true);   // long-press menu (copy / save image / open link)
  document.addEventListener('selectstart', block, true);   // start of a text selection
  document.addEventListener('dragstart', block, true);     // dragging images / links

  // Safety net: some Android WebViews still create a selection — clear it straight away.
  document.addEventListener('selectionchange', function () {
    if (isExempt(document.activeElement)) return;
    var sel = window.getSelection && window.getSelection();
    if (sel && !sel.isCollapsed && sel.rangeCount && !isExempt(sel.anchorNode)) sel.removeAllRanges();
  });
})();
