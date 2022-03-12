import m from 'mithril/hyperscript';
//-
import { Node } from './base';

export class Loading extends Node
{
    MODES = ['default', 'overlay', 'small']

    prepare(vnode, values, context)
    {
        values.txt_loading = gettext("Loading");
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'data-loading': '',
    'class': 'bx--loading',
  },
  m('svg.bx--loading__svg',
    {
      viewBox: '0 0 100 100',
    },
    [
      m('title', null, values.txt_loading),
      m('circle.bx--loading__stroke', {cx: '50%', cy: '50%', r: 44}),
    ]))
//##
        );
    }

    render_overlay(vnode, values, context)
    {
        return (
//##
m('div.bx--loading-overlay', null,
  m('div',
    {
      'data-loading': '',
      'class': 'bx--loading',
    },
    m('svg.bx--loading__svg',
      {
        viewBox: '0 0 100 100',
      },
      [
        m('title', null, values.txt_loading),
        m('circle.bx--loading__stroke', {cx: '50%', cy: '50%', r: 44}),
      ])))
//##
        );
    }

    render_small(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'data-loading': '',
    'class': 'bx--loading bx--loading--small',
  },
  m('svg.bx--loading__svg',
    {
      viewBox: '0 0 100 100',
    },
    [
      m('title', null, values.txt_loading),
      m('circle.bx--loading__background', {cx: '50%', cy: '50%', r: 42}),
      m('circle.bx--loading__stroke', {cx: '50%', cy: '50%', r: 42}),
    ])))
//##
        );
    }
}
