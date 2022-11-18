#include <jni.h>
#include <stdio.h>
#include "b1.h"

JNIEXPORT void JNICALL Java_b1_add(JNIEnv *env, jobject thisObj, int a, int b)
{
  int sum;
  sum = a+b;
  printf("%d + %d = %d",a,b,sum);
  printf("\n");
  return;
}

JNIEXPORT void JNICALL Java_b1_sub(JNIEnv *env, jobject thisObj, int a, int b)
{
  int sub;
  mul = a-b;
  printf("%d - %d = %d",a,b,sub);
  printf("\n");
  return;
}

JNIEXPORT void JNICALL Java_b1_mult(JNIEnv *env, jobject thisObj, int a, int b)
{
  int mult;
  mult = a*b;
  printf("%d * %d = %d",a,b,mult);
  printf("\n");
  return;
}

JNIEXPORT void JNICALL Java_b1_div(JNIEnv *env, jobject thisObj, int a, int b)
{
  int div;
  div = a/b;
  printf("%d / %d = %d",a,b,div);
  printf("\n");
  return;
}
